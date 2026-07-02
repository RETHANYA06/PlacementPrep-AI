from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

import app.session as session
import app.models.interview as interview

from app.services.question_generator import generate_questions
from app.services.answer_evaluator import evaluate_answer
router = APIRouter()


class InterviewRequest(BaseModel):
    company: str
    round_type: str
    difficulty: str
    count: int
class AnswerRequest(BaseModel):
    answer: str

@router.post("/start-interview")
def start_interview(req: InterviewRequest):

    if session.current_profile is None:
        raise HTTPException(
            status_code=400,
            detail="Upload resume first."
        )

    data = generate_questions(
        profile=session.current_profile,
        company=req.company,
        round_type=req.round_type,
        difficulty=req.difficulty,
        count=req.count
    )

    interview.current_interview["questions"] = data["questions"]
    interview.current_interview["answers"] = []
    interview.current_interview["evaluations"] = []
    interview.current_interview["current_question"] = 0
    interview.current_interview["company"] = req.company
    interview.current_interview["round"] = req.round_type
    interview.current_interview["difficulty"] = req.difficulty

    return {
        "message": "Interview started",
        "total_questions": len(data["questions"]),
        "first_question": data["questions"][0]
    }
@router.get("/next-question")
def next_question():

    current = interview.current_interview["current_question"]
    questions = interview.current_interview["questions"]

    if current >= len(questions):
        return {
            "message": "Interview completed"
        }

    return {
        "question_number": current + 1,
        "total_questions": len(questions),
        "question": questions[current]
    }
@router.post("/submit-answer")
def submit_answer(req: AnswerRequest):

    current = interview.current_interview["current_question"]
    questions = interview.current_interview["questions"]

    if current >= len(questions):
        return {
            "message": "Interview already completed."
        }

    question = questions[current]

    evaluation = evaluate_answer(
        question=question,
        answer=req.answer
    )

    interview.current_interview["answers"].append({
        "question": question,
        "answer": req.answer
    })

    interview.current_interview.setdefault("evaluations", []).append(evaluation)

    interview.current_interview["current_question"] += 1

    return {
        "evaluation": evaluation,
        "next_question_number": interview.current_interview["current_question"] + 1,
        "remaining_questions": len(questions) - interview.current_interview["current_question"]
    }