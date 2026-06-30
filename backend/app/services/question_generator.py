import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_questions(profile, round_type="technical", difficulty="medium", count=10):

    prompt = f"""
You are an experienced technical interviewer.

Generate {count} {difficulty}-level interview questions based ONLY on the candidate's resume.

Interview Round:
{round_type}

Rules:
1. Questions must be based only on the candidate profile.
2. Ask project-based and skill-based questions.
3. Do not ask unrelated questions.
4. Do not provide answers.
5. Return ONLY valid JSON.

Output Format:

{{
    "round": "{round_type}",
    "difficulty": "{difficulty}",
    "total_questions": {count},
    "questions": [
        "Question 1",
        "Question 2",
        "Question 3"
    ]
}}

Candidate Profile:

{json.dumps(profile, indent=2)}
"""

    response = model.generate_content(prompt)

    cleaned = (
        response.text
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    return json.loads(cleaned)