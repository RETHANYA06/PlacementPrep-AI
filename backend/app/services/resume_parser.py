import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def parse_resume(text):
    prompt = f"""
Extract information from this resume.

Return ONLY valid JSON.

Schema:

{{
  "name": "",
  "education": "",
  "skills": [],
  "projects": [],
  "experience": []
}}

Resume:
{text}
"""

    response = model.generate_content(prompt)

    cleaned = (
        response.text
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    return json.loads(cleaned)