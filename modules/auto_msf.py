#!/usr/bin/env python3
"""
auto_msf.py

功能：
- 在啟動並互動 msfconsole 前記錄開始時間（本機時區）
- 使用 pexpect 啟動 msfconsole，use 指定 module，set RHOSTS
- 執行 run 並偵測三種結果：
    1) 直接進入 meterpreter prompt
    2) 出現 "Meterpreter session N opened"（但仍為 msf >）
    3) 直接回到 msf > 且沒有 opened 訊息（失敗）
- 透過 sessions -l 確認 session 是否存在（若捕捉到 opened 訊息）
- 在結束時記錄結束時間
- 若失敗，會把所有 console input（腳本下的命令）、console output（msf 的回應）與 framework.log 範圍一起寫入 data/error_message.txt

注意：請在有授權的測試環境執行。僅支援類 Unix（Linux / macOS）環境，需安裝 pexpect。

用法：
    python3 auto_msf.py [module] [rhosts]

預設 module = cve1_md3_test2
預設 rhosts = 192.168.1.114
"""

import os
import sys
import time
import re
from datetime import datetime
import pexpect
import io

# 可調整的參數
DEFAULT_MODULE = "cve1_md3_test2"
DEFAULT_RHOSTS = "192.168.1.114"
PROMPT_REGEX = r"msf.*>\s*$"
LOG_PATH = os.path.expanduser("~/.msf4/logs/framework.log")
OUTPUT_SAVE_PATH = os.path.join("data", "error_message.txt")  # 依你要求存到 data/error_message.txt


def ensure_output_dir(path):
    d = os.path.dirname(path)
    if d and not os.path.exists(d):
        os.makedirs(d, exist_ok=True)


class Tee:
    """簡單的 tee 實作，把寫入內容同時傳到一個 buffer 與 stdout"""

    def __init__(self, buffer, stream=None):
        self.buffer = buffer
        self.stream = stream or sys.stdout

    def write(self, data):
        try:
            self.buffer.write(data)
        except Exception:
            pass
        try:
            self.stream.write(data)
        except Exception:
            pass

    def flush(self):
        try:
            self.buffer.flush()
        except Exception:
            pass
        try:
            self.stream.flush()
        except Exception:
            pass


def parse_log_timestamp(line):
    """嘗試從一行 log 解析時間戳，回傳 datetime 或 None。
    預期格式： [MM/DD/YYYY HH:MM:SS] ...
    """
    m = re.search(r"\[(\d{1,2}/\d{1,2}/\d{4} \d{2}:\d{2}:\d{2})\]", line)
    if not m:
        return None
    ts = m.group(1)
    try:
        dt = datetime.strptime(ts, "%m/%d/%Y %H:%M:%S")
        return dt
    except Exception:
        return None


def extract_log_range(log_path, start_dt, end_dt):
    """從 log_path 中取出時間落在 start_dt..end_dt（含）的行。
    start_dt 和 end_dt 是 naive datetime（系統本地時間）。"""
    if not os.path.exists(log_path):
        return []

    out_lines = []
    timestamp_last = None
    try:
        with open(log_path, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                ts = parse_log_timestamp(line)
                if ts is None:
                    # 若該行沒有 timestamp，若上一個 timestamp 在區間內就保留（處理跨行訊息）
                    if timestamp_last is not None and timestamp_last >= start_dt and timestamp_last <= end_dt:
                        out_lines.append(line)
                    continue
                timestamp_last = ts
                if ts >= start_dt and ts <= end_dt:
                    out_lines.append(line)
    except Exception as e:
        out_lines.append(f"[error reading log file: {e}]\n")
    return out_lines


# patterns for detection
METERPRETER_PROMPT_RE = re.compile(r"meterpreter.*>\s*$", re.IGNORECASE)
SESSION_OPENED_RE = re.compile(r"Meterpreter session (\d+) opened", re.IGNORECASE)
MSF_PROMPT_RE = re.compile(PROMPT_REGEX, re.IGNORECASE)


def run_and_verify(child, commands_sent, total_timeout=60):
    """執行 run 並偵測結果；回傳一個 dict 描述狀態。
    commands_sent: list - 會 append 此函式內額外自動發出的指令（如 background / sessions -l）"""
    # 送出 exploit
    child.sendline("run")
    commands_sent.append("run")
    start = time.time()

    try:
        idx = child.expect([METERPRETER_PROMPT_RE, SESSION_OPENED_RE, MSF_PROMPT_RE], timeout=total_timeout)
    except pexpect.TIMEOUT:
        return {"status": "timeout", "detail": child.before}
    except pexpect.EOF:
        return {"status": "eof", "detail": None}

    # 1) 直接進到 meterpreter prompt
    if idx == 0:
        # 嘗試 background，最多重試幾次以確保回到 msf prompt
        for attempt in range(3):
            commands_sent.append("background")
            child.sendline("background")
            try:
                child.expect(MSF_PROMPT_RE, timeout=8)  # 等待回到 msf prompt
                # 成功回到 msf：檢查 sessions
                commands_sent.append("sessions -l")
                child.sendline("sessions -l")
                child.expect(MSF_PROMPT_RE, timeout=10)
                sessions_out = child.before
                return {"status": "ok", "method": "meterpreter_prompt", "sessions_output": sessions_out}
            except pexpect.TIMEOUT:
                # 仍停在 meterpreter，稍等再試
                time.sleep(1)
                continue
            except pexpect.EOF:
                return {"status": "eof", "detail": None}

        # 反覆 background 仍沒回到 msf prompt：把目前輸出回傳為 maybe（避免直接當作失敗）
        return {"status": "maybe", "method": "meterpreter_prompt_no_bg", "detail": child.before}

    # 2) 捕捉到 opened 訊息（非同步 background 情形）
    if idx == 1:
        session_id = child.match.group(1)
        # 看短暫時間內是否會切換 prompt（不必強求）
        try:
            _ = child.expect([METERPRETER_PROMPT_RE, MSF_PROMPT_RE], timeout=3)
        except Exception:
            pass

        # 嘗試 background（如果仍在 meterpreter）
        commands_sent.append("background")
        try:
            child.sendline("background")
            child.expect(MSF_PROMPT_RE, timeout=8)
        except Exception:
            # 若不能回到 msf，仍繼續嘗試 sessions -l（可能需要在 msf prompt）
            pass

        commands_sent.append("sessions -l")
        child.sendline("sessions -l")
        try:
            child.expect(MSF_PROMPT_RE, timeout=10)
            sessions_out = child.before
        except Exception:
            sessions_out = ""

        if re.search(rf"\b{re.escape(session_id)}\b", sessions_out):
            return {"status": "ok", "method": "session_opened", "session": session_id, "sessions_output": sessions_out}
        else:
            return {"status": "maybe", "method": "opened_but_not_in_list", "session": session_id, "sessions_output": sessions_out}

    # 3) 直接回到 msf prompt（沒有 opened 訊息）
    if idx == 2:
        # 再短暫等待可能的 asynchronous opened 訊息
        try:
            child.expect([SESSION_OPENED_RE], timeout=10)
            session_id = child.match.group(1)
            # 確認 sessions -l
            commands_sent.append("sessions -l")
            child.sendline("sessions -l")
            child.expect(MSF_PROMPT_RE, timeout=10)
            sessions_out = child.before
            if re.search(rf"\b{re.escape(session_id)}\b", sessions_out):
                return {"status": "ok", "method": "opened_after_prompt", "session": session_id, "sessions_output": sessions_out}
            else:
                return {"status": "maybe", "method": "opened_after_prompt_but_not_in_list", "session": session_id, "sessions_output": sessions_out}
        except pexpect.TIMEOUT:
            return {"status": "no_session", "detail": child.before}


def run_auto_msf(module, rhosts, timeout=120):
    # 記錄開始時間（本機時區 naive）
    start_dt = datetime.now()
    print(f"[+] start time: {start_dt.strftime('%Y-%m-%d %H:%M:%S')}")

    # 準備 pexpect，並同時把輸出記錄到 buffer
    buf = io.StringIO()
    tee = Tee(buf, sys.stdout)

    # commands_sent 用來記錄腳本發出的所有命令（console input）
    commands_sent = []

    try:
        print("[*] spawning msfconsole...")
        child = pexpect.spawn("msfconsole", ["-q"], encoding="utf-8", timeout=timeout)
        child.delaybeforesend = 0.05
        child.logfile = tee
    except Exception as e:
        print(f"[!] failed to spawn msfconsole: {e}")
        return 1

    try:
        child.expect(MSF_PROMPT_RE, timeout=timeout)
    except pexpect.exceptions.TIMEOUT:
        print("[!] timeout waiting for prompt")
        child.close(force=True)
        end_dt = datetime.now()
        print(f"[+] end time: {end_dt.strftime('%Y-%m-%d %H:%M:%S')}")
        save_error_artifacts(start_dt, end_dt, buf, commands_sent)
        return 2
    except pexpect.exceptions.EOF:
        print("[!] msfconsole exited unexpectedly (EOF)")
        child.close(force=True)
        end_dt = datetime.now()
        save_error_artifacts(start_dt, end_dt, buf, commands_sent)
        return 3

    try:
        # robust reload_all: 如果失敗記錄但繼續（除非 EOF）
        try:
            print("[*] reload_all")
            commands_sent.append("reload_all")
            child.sendline("reload_all")
            child.expect(MSF_PROMPT_RE, timeout=20)
        except pexpect.TIMEOUT:
            print("[!] reload_all timeout — continuing anyway")
        except pexpect.EOF:
            print("[!] msfconsole EOF during reload_all")
            raise

        print(f"[*] using module: {module}")
        commands_sent.append(f"use {module}")
        child.sendline(f"use {module}")
        child.expect(MSF_PROMPT_RE)

        print(f"[*] set RHOSTS = {rhosts}")
        commands_sent.append(f"set RHOSTS {rhosts}")
        child.sendline(f"set RHOSTS {rhosts}")
        child.expect(MSF_PROMPT_RE)

        print("[*] show options")
        commands_sent.append("show options")
        child.sendline("show options")
        child.expect(MSF_PROMPT_RE)

        print("[*] run exploit and detect result...")
        result = run_and_verify(child, commands_sent, total_timeout=60)

    except pexpect.exceptions.TIMEOUT:
        print("[!] timeout during interaction")
        result = {"status": "error", "detail": "timeout during interaction"}
    except pexpect.exceptions.EOF:
        print("[!] msfconsole EOF during interaction")
        result = {"status": "error", "detail": "EOF during interaction"}
    finally:
        # 嘗試結束（會把 exit 加入 commands_sent 以便紀錄）
        try:
            commands_sent.append("exit")
            child.sendline("exit")
        except Exception:
            pass
        try:
            child.close()
        except Exception:
            pass

    # 記錄結束時間
    end_dt = datetime.now()
    print(f"[+] end time: {end_dt.strftime('%Y-%m-%d %H:%M:%S')}")

    # 取得 pexpect 捕獲的 console 輸出
    console_output = buf.getvalue()

    # 根據 result 判斷並輸出
    status = result.get("status")
    if status == "ok":
        method = result.get("method")
        session = result.get("session")
        print(f"[SUCCESS] exploit resulted in session. method={method} session={session}")
        return 0
    else:
        print(f"[FAILURE] exploit did not produce a usable session. status={status}")
        save_error_artifacts(start_dt, end_dt, console_output, commands_sent)
        return 4


def save_error_artifacts(start_dt, end_dt, console_output, commands_sent):
    """
    將錯誤相關的 artifact 一次寫入檔案：
      - start / end 時間
      - commands_sent（每一行是腳本傳給 msf 的指令）
      - console captured output（pexpect logfile buffer）
      - framework.log 在時間區間內的 slice
    """
    # 取出 framework.log 的範圍行
    log_lines = extract_log_range(LOG_PATH, start_dt, end_dt)

    ensure_output_dir(OUTPUT_SAVE_PATH)
    try:
        with open(OUTPUT_SAVE_PATH, "w", encoding="utf-8") as fo:
            fo.write(f"# start {start_dt.isoformat()}\n")
            fo.write(f"# end   {end_dt.isoformat()}\n")
            fo.write("\n# ===== commands sent (console input) =====\n")
            if commands_sent:
                for c in commands_sent:
                    fo.write(c.rstrip() + "\n")
            else:
                fo.write("[no commands recorded]\n")

            fo.write("\n# ===== console captured output (stdout/stderr) =====\n")
            fo.write(console_output + "\n")

            fo.write("\n# ===== framework.log slice =====\n")
            if log_lines:
                fo.writelines(log_lines)
            else:
                fo.write("[no log lines found in the selected interval or log file missing]\n")

        print(f"[+] saved error artifacts to {OUTPUT_SAVE_PATH}")
    except Exception as e:
        print(f"[!] failed to save error artifacts: {e}")


if __name__ == "__main__":
    module_arg = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_MODULE
    rhosts_arg = sys.argv[2] if len(sys.argv) > 2 else DEFAULT_RHOSTS
    rc = run_auto_msf(module_arg, rhosts_arg, timeout=120)
    sys.exit(rc)
