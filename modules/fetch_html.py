# modules/fetch_html.py
from playwright.sync_api import sync_playwright, TimeoutError as PWTimeout
from pathlib import Path
from typing import Optional
import time

def fetch_html(url: str, html_path: Path, debug: bool = False, retries: int = 1, timeout_ms: int = 60000, wait_after_ms: int = 500) -> Optional[str]:
    """
    使用 Playwright 抓取 url 的完整 HTML，等待 networkidle。
    回傳 HTML 字串或 None（若全部失敗）。
    """
    attempt = 0
    while attempt < retries:
        attempt += 1
        try:
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)
                context = browser.new_context()
                page = context.new_page()
                if debug:
                    print(f"[Attempt {attempt}/{retries}] Navigating to {url} ...")
                page.goto(url, timeout=timeout_ms, wait_until="domcontentloaded")
                try:
                    page.wait_for_load_state("networkidle", timeout=timeout_ms)
                except PWTimeout:
                    if debug:
                        print(f"  warning: networkidle timeout after {timeout_ms} ms (attempt {attempt}). Continuing...")
                time.sleep(wait_after_ms / 1000.0)
                html = page.content()
                if debug:
                    html_path.write_text(html, encoding="utf-8")
                    print(f"Saved HTML to {html_path}")
                try:
                    context.close()
                    browser.close()
                except Exception:
                    pass
                return html
        except Exception as e:
            print(f"  error on attempt {attempt}: {e}")
            backoff = 1.5 ** attempt
            if debug:
                print(f"  retrying after {backoff:.1f}s ...")
            time.sleep(backoff)
    print("All attempts failed.")
    return None
