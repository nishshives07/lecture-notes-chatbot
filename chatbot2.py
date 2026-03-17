import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key
load_dotenv()
api_key =os.getenv("GEMINI_API_KEY")

genai.configure(api_key="AIzaSyC0_SWlmV3OndK72MD6eKebjQMe6qtUBE8")

model = genai.GenerativeModel("gemini-1.5-flash")  # updated model

print("📘 Paste your lecture notes:")
notes = input()

# -------- SUMMARY --------
prompt = f"""
Summarize these notes:
- Title
- 3-5 key points
- Action items

Notes:
{notes}
"""

try:
    response = model.generate_content(prompt)
    print("\n📌 Summary:\n", response.text)
except Exception as e:
    print("⚠️ Error:", e)


