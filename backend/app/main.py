from fastapi import FastAPI

from app.routes.resume import router as resume_router
from app.routes.questions import router as questions_router

app = FastAPI(title="PlacementPrep AI")

app.include_router(resume_router)
app.include_router(questions_router)


@app.get("/")
def home():
    return {
        "message": "PlacementPrep AI Backend Running"
    }