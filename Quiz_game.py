questions = {
    "Which language is used for AI? ": "python",
    "What does CPU stand for? ": "central processing unit",
    "Which symbol starts a Python comment? ": "#",
    "What is 5 * 6? ": "30"
}

score = 0

for question, answer in questions.items():
    user_answer = input(question).lower().strip()

    if user_answer == answer:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print("\nFinal Score:", score, "/", len(questions))
print("Percentage:", (score / len(questions)) * 100, "%")
