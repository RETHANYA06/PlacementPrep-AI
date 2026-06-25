import google.generativeai as genai
import json
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")
genai.configure(api_key="YOUR_GEMINI_API_KEY")

model = genai.GenerativeModel("gemini-2.5-flash")


def parse_resume(text):

    prompt = f"""
    Extract the following information from the resume.

    Return ONLY valid JSON.

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

    return response.text