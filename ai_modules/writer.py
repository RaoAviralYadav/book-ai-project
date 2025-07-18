
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


model = genai.GenerativeModel("models/gemini-2.5-pro")

def spin_chapter(content):
    
    response = model.generate_content(
        contents=[{
            "role": "user",
            "parts": [f"Rewrite this chapter to make it more modern, vivid, and engaging:\n\n{content}"]
        }]
    )
    return response.text
