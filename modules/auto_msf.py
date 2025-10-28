#!/usr/bin/env python3
# modules/auto_msf.py
"""
自動化啟動 msfconsole、use module、set RHOSTS、print show options
改良版：更寬鬆的 prompt regex、較長 timeout、並把 pexpect 的原始輸出印出來以利 debug
請在 Linux/macOS 上執行並在有授權的環境測試。
"""

import pexpect
import sys
import time
import re

# 比較寬鬆的 prompt regex：匹配如 "msf >"、"msf > "、或帶些顏色字元的情況
PROMPT_REGEX = r"msf.*>\s*$"

def run_auto_msf(module="auxiliary/scanner/ssh/ssh_version", rhosts="192.168.1.114", timeout=120):
    try:
        print("[*] 啟動 msfconsole...")
        # spawn 時不使用 shell 讓行為較一致
        child = pexpect.spawn("msfconsole", ["-q"], encoding="utf-8", timeout=timeout)
        # 把 pexpect 收到的原始輸出也輸出到 stdout（方便 debug）
        child.logfile = sys.stdout
        # 少量延遲（pexpect 在 sendline 前的 delay）
        child.delaybeforesend = 0.05
    except Exception as e:
        print("[!] 無法 spawn msfconsole，錯誤：", e)
        return 1

    try:
        # 使用 regex 等待 prompt。多給一些時間，不要用 exact match。
        print("[*] 等待 msf prompt (regex):", PROMPT_REGEX)
        # 先嘗試更寬鬆匹配多次，處理 banner 輸出過長的情況
        child.expect(re.compile(PROMPT_REGEX), timeout=timeout)
    except pexpect.exceptions.TIMEOUT:
        print("[!] 等待 msf prompt 超時，請檢查：")
        print("    1) msfconsole 是否能在此使用者/環境啟動 (試在同一 shell 執行 `msfconsole -q`)。")
        print("    2) PATH 是否正確 (腳本內的 msfconsole 路徑是否同 manual 相同)。")
        print("    3) 若 msf 輸出大量 banner/更新訊息，請增加 timeout。")
        # child.logfile 已經把輸出印出來，這邊再關閉
        child.close(force=True)
        return 2
    except pexpect.exceptions.EOF:
        print("[!] msfconsole 提早結束 (EOF)。可能是啟動錯誤或二進位無法執行。")
        child.close(force=True)
        return 3

    try:
        print("[*] 使用 module:", module)
        child.sendline(f"use {module}")
        child.expect(re.compile(PROMPT_REGEX))
        # child.before 包含 use 指令的回傳（已被 logfile 印過，但這裡仍可存取）
        print("--- use output (above) ---")

        print(f"[*] 設定 RHOSTS = {rhosts}")
        child.sendline(f"set RHOSTS {rhosts}")
        child.expect(re.compile(PROMPT_REGEX))
        print("--- set output (above) ---")

        print("[*] 顯示 options 以確認設定")
        child.sendline("show options")
        child.expect(re.compile(PROMPT_REGEX))
        # 這時 child.before 包含 show options 的輸出
        print("----- show options output (captured) -----")
        print(child.before.strip())
        print("----- end -----")

    except pexpect.exceptions.TIMEOUT:
        print("[!] 與 msfconsole 互動時發生 timeout（某步驟花太久）")
        child.close(force=True)
        return 4
    except pexpect.exceptions.EOF:
        print("[!] msfconsole 提早終止（EOF） during interaction")
        child.close(force=True)
        return 5
    finally:
        # 嘗試乾淨結束
        try:
            child.sendline("exit")
        except Exception:
            pass
        child.close()

    print("[*] 完成")
    return 0

if __name__ == "__main__":
    # 可由 CLI 傳 module 與 rhosts
    module_arg = sys.argv[1] if len(sys.argv) > 1 else "auxiliary/scanner/ssh/ssh_version"
    rhosts_arg = sys.argv[2] if len(sys.argv) > 2 else "192.168.1.114"
    rc = run_auto_msf(module=module_arg, rhosts=rhosts_arg, timeout=120)
    sys.exit(rc)
