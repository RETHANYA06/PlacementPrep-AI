from fastapi import APIRouter
from pydantic import BaseModel
from app.services.question_generator import generate_questions

router = APIRouter()


class QuestionRequest(BaseModel):
    profile: dict
    round_type: str = "technical"
    difficulty: str = "medium"
    count: int = 10


@router.post("/generate-questions")
def generate(req: QuestionRequest):

    questions = generate_questions(
        profile=req.profile,
        round_type=req.round_type,
        difficulty=req.difficulty,
        count=req.count
    )

    return questions