from fastapi import FastAPI
from app.routes.evaluator import router as evaluator_router
from app.routes.resume import router as resume_router
from app.routes.questions import router as questions_router
from app.routes.interview import router as interview_router
from app.routes.answer import router as answer_router
app = FastAPI(title="PlacementPrep AI")

app.include_router(resume_router)
app.include_router(questions_router)
app.include_router(interview_router)
app.include_router(evaluator_router)
app.include_router(answer_router)

@app.get("/")
def home():
    return {
        "message": "PlacementPrep AI Backend Running"
    }