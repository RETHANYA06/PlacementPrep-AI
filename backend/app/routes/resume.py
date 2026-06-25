from fastapi import APIRouter, UploadFile, File
import os
import fitz
from app.services.resume_parser import parse_resume

router = APIRouter()

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        content = await file.read()
        buffer.write(content)

    pdf = fitz.open(file_path)

    extracted_text = ""

    for page in pdf:
        extracted_text += page.get_text()

    pdf.close()

    profile = parse_resume(extracted_text)

    return {
        "message": "Resume uploaded successfully",
        "filename": file.filename,
        "profile": profile
    }