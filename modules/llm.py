from g4f.client import Client
import os
import requests

def generate_response(prompt: str, model: str = "gemini-2.0-flash", web_search: bool = False) -> str:
    if model == "gemini-2.0-flash":
        GEMINI_API_KEY = os.getenv("GEMINI_KEY")
        if not GEMINI_API_KEY:
            raise ValueError("Please set GEMINI_KEY environment variable to use gemini generation")

        # 下面以 google.generativeai 為例（與你原本的類似）
        try:
            import google.generativeai as genai
        except ImportError:
            raise ImportError("Please install google-generative-ai package to use gemini generation")
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content(prompt)
        return response.text
    
    local_model = ["llama3.3:latest", "gemma3:4b", "gemma2:9b", "phi3:latest", "gemma3:27b", "gpt-oss:latest", "llama3.3:70b"]
    if model in local_model:
        url = "http://localhost:11434/api/generate"
        payload = {
            "model": model,
            "prompt": prompt,
            "stream": False
        }
        response = requests.post(url, json=payload)
        return response.json().get("response")
    else:
        url = "http://192.168.1.116:1337/v1/chat/completions"
        body = {
            "provider": "HuggingFaceAPI",
            "model": model,
            # "stream": False,
            "api_key": os.getenv("HUGGINGFACE_API_KEY"),     # 換成你的 HuggingFace Token

            "messages": [{"role": "user", "content": prompt}],
            # g4f docker API 可能沒有 web_search 參數，如果你的版本支援可加
            # "web_search": web_search  
        }

        response = requests.post(url, json=body)
        response.raise_for_status()  # 若 HTTP 錯誤會丟例外

        choices = response.json().get("choices", [])
        if not choices:
            return ""  # 沒有回覆就回空字串

        # 取第一個 choice 的 content
        return choices[0].get("message", {}).get("content", "")

