#!/usr/bin/env python3

from pathlib import Path
import argparse
import os
import google.generativeai as genai
import re

try:
    from html2md import html_to_markdown
    from gethtml import fetch_html
except Exception as e:
    print("import error: ", e)
    raise

DEFAULT_HTML_PATH = Path("output.html")
DEFAULT_OUTPUT_PATH = Path("output.md")
exploit_filename = "auto_generated_exploit.rb"
exploit_dir = "exploit_modules"  # 你的 Metasploit module 存放資料夾
exploit_path = os.path.join(exploit_dir, exploit_filename)

def extract_code_best_effort(text: str) -> str | None:
    # 1) 優先找 ```ruby
    m = re.findall(r"```ruby\s*(.*?)```", text, re.IGNORECASE | re.DOTALL)
    if m:
        # 如有多個 ruby fence，挑最長（通常是程式碼）
        return max(m, key=len).strip()

    # 2) 找任意 code fence（第一個或挑最長）
    m_all = re.findall(r"```(?:[^\n]*)\n(.*?)```", text, re.DOTALL)
    if m_all:
        return max(m_all, key=len).strip()

    # 3) fallback：找 class MetasploitModule 開頭直到檔尾（或下一個 ```）
    m = re.search(r"(class\s+MetasploitModule\b.*)", text, re.DOTALL)
    if m:
        return m.group(1).strip()

    return None

def genRb(markdown_content: str, debug: bool = False, FirstTry: bool = True):
    GEMINI_API_KEY = os.getenv("GEMINI_KEY")
    if not GEMINI_API_KEY:
        raise ValueError("Please set GEMINI_KEY environment variable")

    genai.configure(api_key=GEMINI_API_KEY)

    # ==== 初始化 Gemini 模型 ====
    model = genai.GenerativeModel("gemini-2.0-flash")

    # ==== 生成 prompt ====
    prompt = ""
    if FirstTry is True:
        with open('InitPrompt.txt', 'r', encoding='utf-8') as f:
            prompt = f.read()
    else:
        with open(exploit_path, 'r', encoding='utf-8') as f:
            existing_code = f.read()
        with open('errorMsg.txt', 'r', encoding='utf-8') as f:
            error_msg = f.read()
        with open('retryPrompt.txt', 'r', encoding='utf-8') as f:
            prompt = existing_code + "\n Error msg: " + error_msg + "\n" + f.read()
    prompt += markdown_content

    # ==== 呼叫 Gemini API 生成 Ruby 程式碼 ====
    response = model.generate_content(prompt)
    ruby_code = response.text  # genai 套件回傳的文字
    next_url = None
    match = re.match(r'(https?://\S+)', ruby_code)
    if match:
        next_url = match.group(1)
    print(next_url)
    if next_url:
        with open("next_url.txt", "w", encoding="utf-8") as f:
            f.write(next_url + "\n")
    if debug:
        print("=== Gemini Response ===")
        print(ruby_code)
        print("=======================")
    extracted = extract_code_best_effort(ruby_code)

    # ==== 寫入 .rb 檔案 ====
    
    os.makedirs(exploit_dir, exist_ok=True)

    
    with open(exploit_path, "w", encoding="utf-8") as f:
        if extracted is not None:
            f.write(extracted)
            print(f"[+] Exploit generated and saved to: {exploit_path}")
        else:
            print("Warning: 無法從生成的內容中提取 Ruby 程式碼，將寫入完整回應內容。")

def main():
    parser = argparse.ArgumentParser(
        description="Fetch HTML from URL and convert to Markdown"
    )
    parser.add_argument("--retry", action='store_true', help="Whether this is a retry attempt")
    parser.add_argument("--html-out", type=Path, default=DEFAULT_HTML_PATH, help="Path to save HTML")
    parser.add_argument("--md-out", type=Path, default=DEFAULT_OUTPUT_PATH, help="Path to save Markdown")
    parser.add_argument("--debug", action="store_true", help="Enable debug mode")
    args = parser.parse_args()

    if args.debug:
        print("Debug mode enabled.")
    md_out = args.md_out
    with open("next_url.txt", "r", encoding="utf-8") as f:
        urls = [line.strip() for line in f if line.strip()]
    print(f"Read {len(urls)} URLs from next_url.txt")
    for url in urls:        print("  ", url)

    url = urls[0] if urls else None
    html_out = args.html_out
    if not (url.startswith("http://") or url.startswith("https://")):
        raise ValueError(f"Invalid URL: {url}")

    html = fetch_html(url, html_out, args.debug)
    if not html:
        raise ValueError("Failed to fetch HTML")
    
    md = html_to_markdown(html)
    md_out.write_text(md, encoding="utf-8") # save md file
    print(f"Wrote {len(md)} characters to {md_out}")
    
    genRb(md, debug=args.debug)
    print("Done.")


if __name__ == "__main__":
    main()
