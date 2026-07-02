import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def evaluate_answer(question, answer):

    prompt = f"""
You are a senior technical interviewer.

Evaluate the candidate's answer.

Question:
{question}

Candidate Answer:
{answer}

Score the answer out of 10.

Return ONLY valid JSON.

Schema:

{{
    "score": 0,
    "strengths": [],
    "improvements": [],
    "ideal_answer": ""
}}
"""

    response = model.generate_content(prompt)

    cleaned = (
        response.text
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    return json.loads(cleaned)