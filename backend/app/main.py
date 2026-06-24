from fastapi import FastAPI

app = FastAPI(title="PlacementPrep AI")


@app.get("/")
def home():
    return {
        "message": "PlacementPrep AI Backend Running"
    }