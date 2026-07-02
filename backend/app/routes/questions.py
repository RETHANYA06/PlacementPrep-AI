from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

import app.session as session
from app.services.question_generator import generate_questions

router = APIRouter()


class QuestionRequest(BaseModel):
    company: str = "General"
    round_type: str = "technical"
    difficulty: str = "medium"
    count: int = 10


@router.post("/generate-questions")
def generate(req: QuestionRequest):

    if session.current_profile is None:
        raise HTTPException(
            status_code=400,
            detail="Upload a resume first."
        )
    print(session.current_profile)
    return generate_questions(
        profile=session.current_profile,
    round_type=req.round_type,
    difficulty=req.difficulty,
    company=req.company,
    count=req.count
    )