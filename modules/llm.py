from g4f.client import Client
import os

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
    
    client = Client()
    response = client.chat.completions.create(
        model=model, # Try "gpt-4o", "deepseek-v3", etc.
        messages=[{"role": "user", "content": prompt}],
        web_search=web_search
    )
    return response.choices[0].message.content

