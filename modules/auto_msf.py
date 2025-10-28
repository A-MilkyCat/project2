#!/usr/bin/env python3
"""
auto_msf.py

功能：
- 在啟動並互動 msfconsole 前記錄開始時間（本機時區）
- 使用 pexpect 啟動 msfconsole，use 指定 module，set RHOSTS
- 執行 show options 並安全退出
- 在結束時記錄結束時間
- 若在 pexpect capture 的 console 輸出中**沒有**出現 "Meterpreter session 1 opened"，
  則從 ~/.msf4/logs/framework.log 取出介於開始/結束時間之間的 log 行，並存到 ../data/error_message.txt

注意：請在有授權的測試環境執行。僅支援類 Unix（Linux / macOS）環境，需安裝 pexpect。

用法：
    python3 auto_msf.py [module] [rhosts]

預設 module = auxiliary/scanner/ssh/ssh_version
預設 rhosts = 192.168.1.114
"""

import os
import sys
import time
import re
from datetime import datetime
from zoneinfo import ZoneInfo
import pexpect
import io

# 可調整的參數
DEFAULT_MODULE = "auxiliary/scanner/ssh/ssh_version"
DEFAULT_RHOSTS = "192.168.1.114"
PROMPT_REGEX = r"msf.*>\s*$"
LOG_PATH = os.path.expanduser("~/.msf4/logs/framework.log")
OUTPUT_SAVE_PATH = os.path.join("data", "error_message.txt")


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
    支援格式：[MM/DD/YYYY HH:MM:SS] ...
    """
    m = re.search(r"\[(\d{1,2}/\d{1,2}/\d{4} \d{2}:\d{2}:\d{2})\]", line)
    if not m:
        return None
    ts = m.group(1)
    try:
        dt = datetime.strptime(ts, "%m/%d/%Y %H:%M:%S")
        # 解析出的時間視為本機時區（與 msf/process 相同）
        return dt
    except Exception:
        return None


def extract_log_range(log_path, start_dt, end_dt):
    """從 log_path 中取出時間落在 start_dt..end_dt（含）的行。
    start_dt 和 end_dt 是 naive datetime（系統本地時間）或 timezone-aware；此函式會比對 naive。"""
    if not os.path.exists(log_path):
        return []

    out_lines = []
    try:
        with open(log_path, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                ts = parse_log_timestamp(line)
                if ts is None:
                    # 若該行沒有 timestamp，若已經在區間內就保留（處理多行訊息被換行的情況）
                    if out_lines and 'timestamp_last' in locals() and timestamp_last is not None:
                        if timestamp_last >= start_dt and timestamp_last <= end_dt:
                            out_lines.append(line)
                    continue
                timestamp_last = ts
                # 比對（將 start/end 與 ts 視為 naive 本地時間）
                if ts >= start_dt and ts <= end_dt:
                    out_lines.append(line)
    except Exception as e:
        out_lines.append(f"[error reading log file: {e}]\n")
    return out_lines


def run_auto_msf(module, rhosts, timeout=120):
    # 記錄開始時間（本機時區 naive）
    start_dt = datetime.now()
    print(f"[+] start time: {start_dt.strftime('%Y-%m-%d %H:%M:%S')}")

    # 準備 pexpect，並同時把輸出記錄到 buffer
    buf = io.StringIO()
    tee = Tee(buf, sys.stdout)

    try:
        print("[*] spawning msfconsole...")
        child = pexpect.spawn("msfconsole", ["-q"], encoding="utf-8", timeout=timeout)
        child.delaybeforesend = 0.05
        child.logfile = tee
    except Exception as e:
        print(f"[!] failed to spawn msfconsole: {e}")
        return 1

    try:
        child.expect(re.compile(PROMPT_REGEX), timeout=timeout)
    except pexpect.exceptions.TIMEOUT:
        print("[!] timeout waiting for prompt")
        child.close(force=True)
        end_dt = datetime.now()
        print(f"[+] end time: {end_dt.strftime('%Y-%m-%d %H:%M:%S')}")
        # 如果無法取得 prompt，也把該時間區間的 log 存下
        save_log_slice_if_no_meterpreter(start_dt, end_dt, buf)
        return 2
    except pexpect.exceptions.EOF:
        print("[!] msfconsole exited unexpectedly (EOF)")
        child.close(force=True)
        end_dt = datetime.now()
        save_log_slice_if_no_meterpreter(start_dt, end_dt, buf)
        return 3

    try:
        print(f"[*] reload all")
        child.sendline(f"reload_all")
        child.expect(re.compile(PROMPT_REGEX))

        print(f"[*] using module: {module}")
        child.sendline(f"use {module}")
        child.expect(re.compile(PROMPT_REGEX))

        print(f"[*] set RHOSTS = {rhosts}")
        child.sendline(f"set RHOSTS {rhosts}")
        child.expect(re.compile(PROMPT_REGEX))

        print("[*] show options")
        child.sendline("show options")
        child.expect(re.compile(PROMPT_REGEX))

        # 若需要，你可以在此加入其他指令（例如 run 或 check），但本範例避免執行 exploit

    except pexpect.exceptions.TIMEOUT:
        print("[!] timeout during interaction")
    except pexpect.exceptions.EOF:
        print("[!] msfconsole EOF during interaction")
    finally:
        # 嘗試結束
        try:
            child.sendline("exit")
        except Exception:
            pass
        # 等待 child 真正結束
        try:
            child.close()
        except Exception:
            pass

    # 記錄結束時間
    end_dt = datetime.now()
    print(f"[+] end time: {end_dt.strftime('%Y-%m-%d %H:%M:%S')}")

    # 取得 pexpect 捕獲的 console 輸出
    console_output = buf.getvalue()

    # 判斷是否出現 "Meterpreter session 1 opened"
    if "Meterpreter session 1 opened" in console_output:
        print("[+] found Meterpreter session message in console output")
        return 0
    else:
        print("[-] no Meterpreter session message in console output; saving relevant log slice...")
        save_log_slice_if_no_meterpreter(start_dt, end_dt, buf)
        return 4


def save_log_slice_if_no_meterpreter(start_dt, end_dt, buf):
    # 讀取並過濾 framework.log
    # 將 start_dt/end_dt 轉為同樣格式的 naive datetime（log 是 MM/DD/YYYY ...）
    # 這裡我們假設 log 的 timestamp 與系統本地時間一致

    # 讀 log 並取出時間範圍內的行
    log_lines = extract_log_range(LOG_PATH, start_dt, end_dt)

    ensure_output_dir(OUTPUT_SAVE_PATH)
    try:
        with open(OUTPUT_SAVE_PATH, "w", encoding="utf-8") as fo:
            fo.write(f"# start {start_dt.isoformat()}\n")
            fo.write(f"# end   {end_dt.isoformat()}\n")
            fo.write("# console captured output:\n")
            fo.write(buf.getvalue())
            fo.write("\n# framework.log slice:\n")
            if log_lines:
                fo.writelines(log_lines)
            else:
                fo.write("[no log lines found in the selected interval or log file missing]\n")
        print(f"[+] saved log slice to {OUTPUT_SAVE_PATH}")
    except Exception as e:
        print(f"[!] failed to save log slice: {e}")


if __name__ == "__main__":
    module_arg = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_MODULE
    rhosts_arg = sys.argv[2] if len(sys.argv) > 2 else DEFAULT_RHOSTS
    rc = run_auto_msf(module_arg, rhosts_arg, timeout=120)
    sys.exit(rc)
