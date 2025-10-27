from bs4 import BeautifulSoup
import html2text

def html_to_markdown(html: str) -> str:
    # 預先清理多餘空白（模擬 >\s+< 與 \s+）
    html = ' '.join(html.replace('>\n<', '><').split())

    # 用 BeautifulSoup 過濾掉 script, style, noscript, meta, link
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "noscript", "meta", "link"]):
        tag.decompose()

    # 初始化 html2text
    h2t = html2text.HTML2Text()
    h2t.body_width = 0  # 不要自動換行
    h2t.ignore_links = False

    # 自訂標籤處理
    # BeautifulSoup 先轉換特殊規則
    for p in soup.find_all("p"):
        p.insert_before("\n\n")
        p.insert_after("\n\n")

    for div in soup.find_all("div"):
        if div.get_text(strip=True):
            div.insert_before("\n\n")
            div.insert_after("\n\n")

    for br in soup.find_all("br"):
        br.insert_before("\n")

    # inline tags 處理：em/i → *text* , strong/b → **text**
    for em in soup.find_all(["em", "i"]):
        em.string = f"*{em.get_text(strip=True)}*"

    for strong in soup.find_all(["strong", "b"]):
        strong.string = f"**{strong.get_text(strip=True)}**"

    # span → 保留純文字
    for span in soup.find_all("span"):
        span.replace_with(span.get_text(strip=True))

    # 轉成 markdown
    markdown = h2t.handle(str(soup))
    return markdown.strip()


# ======= 測試用 =======
if __name__ == "__main__":
    with open("example.html", "r", encoding="utf-8") as f:
        html = f.read()
    markdown = html_to_markdown(html)

    out_path = "output.md"   # 你要寫成 "output" 也可以，這裡用 .md 比較直觀
    with open(out_path, "w", encoding="utf-8") as out:
        out.write(markdown)

    print(f"Wrote {len(markdown)} characters to {out_path}")

