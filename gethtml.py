# Playwright sync API
from playwright.sync_api import sync_playwright, TimeoutError as PWTimeout
from pathlib import Path
from typing import Optional
import time

def fetch_html(url: str, html_path: Path, debug: bool = False, retries: int = 3, timeout_ms: int = 60000, wait_after_ms: int = 500) -> Optional[str]:
    """
    使用 Playwright（sync）抓取 url 的完整 HTML，會等待 networkidle。
    - retries: 重試次數
    - timeout_ms: page.wait_for_load_state('networkidle') 的 timeout 毫秒
    - wait_after_ms: 在 page.content() 前再等短暫時間以確保 JS 操作收尾
    回傳 HTML 字串或 None（若全部失敗）。
    """
    attempt = 0
    while attempt < retries:
        attempt += 1
        try:
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)
                context = browser.new_context()  # 可在此加 user_agent 或 viewport
                page = context.new_page()
                print(f"[Attempt {attempt}/{retries}] Navigating to {url} ...")
                page.goto(url, timeout=timeout_ms, wait_until="domcontentloaded")
                # 等待 network idle（網路空閒）通常能等待 SPA / 動態內容渲染
                try:
                    page.wait_for_load_state("networkidle", timeout=timeout_ms)
                except PWTimeout:
                    # networkidle 超時，但 DOM 可能還可用；繼續且稍微等待
                    print(f"  warning: networkidle timeout after {timeout_ms} ms (attempt {attempt}). Continuing...")
                # 額外短暫等待，讓前端 JS 有時間收尾（可視需求調整）
                time.sleep(wait_after_ms / 1000.0)
                html = page.content()  # 取得完整 HTML (含渲染後)
                # 儲存到檔案
                if debug:
                    print(f"Debug: Saving HTML to {html_path}")
                    html_path.write_text(html, encoding="utf-8")
                try:
                    context.close()
                    browser.close()
                except Exception:
                    pass
                return html
        except Exception as e:
            print(f"  error on attempt {attempt}: {e}")
            backoff = 1.5 ** attempt
            print(f"  retrying after {backoff:.1f}s ...")
            time.sleep(backoff)
    print("All attempts failed.")
    return None