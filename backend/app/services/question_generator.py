import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_questions(
    profile,
    round_type="technical",
    difficulty="medium",
    company="General",
    count=10
):

    prompt = f"""
You are a senior interviewer at {company}.

Generate {count} {difficulty}-level interview questions.

Interview Round:
{round_type}

Rules:
1. The questions must match the interview style of {company}.
2. Questions must be based ONLY on the candidate's resume.
3. Include project-based questions.
4. Include skill-based questions.
5. Do NOT provide answers.
6. Return ONLY valid JSON.

Output Format:

{{
    "company": "{company}",
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