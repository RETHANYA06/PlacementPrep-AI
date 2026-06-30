from app.services.question_generator import generate_questions

profile = {
    "name": "Rethanya V",
    "skills": [
        "Python",
        "FastAPI",
        "C++",
        "DSA"
    ],
    "projects": [
        "PlacementPrep AI",
        "GermanPath AI"
    ]
}

result = generate_questions(profile)

print(result)