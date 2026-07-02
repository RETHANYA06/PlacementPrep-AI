from app.services.answer_evaluator import evaluate_answer

question = "Explain OOP."

answer = """
Object Oriented Programming is a programming paradigm.

It has four principles:

Encapsulation
Inheritance
Polymorphism
Abstraction

It improves code reuse and maintainability.
"""

result = evaluate_answer(question, answer)

print(result)