from fastapi import FastAPI
from app.routes.resume import router as resume_router

app = FastAPI(title="PlacementPrep AI")

app.include_router(resume_router)

@app.get("/")
def home():
    return {
        "message": "PlacementPrep AI Backend Running"
    }