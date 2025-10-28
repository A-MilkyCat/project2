#!/usr/bin/env python3
# auo_msf.py
# 目的：示範如何自動化啟動 msfconsole、use module、set RHOSTS、並印出 show options
# 注意：僅示範自動化，不會執行 exploit。請在有授權的環境下執行。

import pexpect
import sys
import time

MSF_PROMPT = "msf >"

def run_auto_msf(module="auxiliary/scanner/ssh/ssh_version", rhosts="192.168.1.114", timeout=30):
    try:
        print("[*] 啟動 msfconsole...")
        child = pexpect.spawn("msfconsole -q", encoding="utf-8", timeout=timeout)
    except Exception as e:
        print("[!] 無法啟動 msfconsole，錯誤：", e)
        return 1

    try:
        # 等候 prompt（有時 banner 很長，可能要等一會）
        child.expect(MSF_PROMPT)
    except pexpect.exceptions.TIMEOUT:
        print("[!] 等待 msf prompt 超時，請確認 msfconsole 是否可啟動並且系統 PATH 有 msfconsole。")
        child.close(force=True)
        return 2

    try:
        print("[*] 使用 module:", module)
        child.sendline(f"use {module}")
        child.expect(MSF_PROMPT)
        print(child.before.strip())  # use 指令的輸出

        print(f"[*] 設定 RHOSTS = {rhosts}")
        child.sendline(f"set RHOSTS {rhosts}")
        child.expect(MSF_PROMPT)
        print(child.before.strip())  # set 指令的輸出

        print("[*] 顯示 options 以確認設定")
        child.sendline("show options")
        child.expect(MSF_PROMPT)
        show_output = child.before.strip()
        print("----- show options output -----")
        print(show_output)
        print("----- end -----")

    except pexpect.exceptions.EOF:
        print("[!] msfconsole 提早終止（EOF）")
        child.close(force=True)
        return 3
    except pexpect.exceptions.TIMEOUT:
        print("[!] 與 msfconsole 互動時發生 timeout")
        child.close(force=True)
        return 4
    finally:
        # 乾淨結束
        try:
            child.sendline("exit")
        except Exception:
            pass
        child.close()

    print("[*] 完成")
    return 0

if __name__ == "__main__":
    # 可從 command line 傳 module 與 rhosts： python auo_msf.py auxiliary/scanner/ssh/ssh_version 192.168.1.114
    module_arg = sys.argv[1] if len(sys.argv) > 1 else "auxiliary/scanner/ssh/ssh_version"
    rhosts_arg = sys.argv[2] if len(sys.argv) > 2 else "192.168.1.114"
    rc = run_auto_msf(module=module_arg, rhosts=rhosts_arg, timeout=30)
    sys.exit(rc)
