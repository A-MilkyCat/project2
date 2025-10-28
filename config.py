# config.py
from pathlib import Path

ROOT = Path(__file__).resolve().parent

# I/O 路徑（放在 data/）
DATA_DIR = ROOT / "data"
PROMPTS_DIR = ROOT / "prompts"
DATA_DIR.mkdir(exist_ok=True)
PROMPTS_DIR.mkdir(exist_ok=True)

OUTPUT_JSON = DATA_DIR / "output.json"
NEXT_URL_TXT = DATA_DIR / "next_url.txt"
OUTPUT_HTML = DATA_DIR / "output.html"
OUTPUT_MD = DATA_DIR / "output.md"

INITPROMPT = PROMPTS_DIR / "init_prompt.txt"
RETRYPROMPT = PROMPTS_DIR / "retry_prompt.txt"
ERRORMSG = PROMPTS_DIR / "error_message.txt"

# 生成 exploit 的目錄與檔名
EXPLOIT_DIR = ROOT / "exploit_modules"
EXPLOIT_DIR.mkdir(exist_ok=True)
EXPLOIT_FILENAME = "auto_generated_exploit.rb"
EXPLOIT_PATH = EXPLOIT_DIR / EXPLOIT_FILENAME

# 其他常數
MAXIMUM_URLS = 3
