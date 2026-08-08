# ----------------------------------------------------------
# Program : Quiz Game
# Author  : G. Sanjansah
# Purpose : Conduct a multiple-choice quiz and calculate
#           the final score and percentage.
# ----------------------------------------------------------

# Store all quiz questions in a list.
# Each question is represented as a dictionary.
questions = [
    {
        "question": "What is the capital of India?",
        "options": [
            "A. Delhi",
            "B. Mumbai",
            "C. Chennai",
            "D. Kolkata"
        ],
        "answer": "A"
    },
    {
        "question": "Which language is used for AI the most?",
        "options": [
            "A. Java",
            "B. Python",
            "C. C",
            "D. PHP"
        ],
        "answer": "B"
    },
    {
        "question": "How many days are there in a leap year?",
        "options": [
            "A. 364",
            "B. 365",
            "C. 366",
            "D. 367"
        ],
        "answer": "C"
    },
    {
        "question": "Who developed Python?",
        "options": [
            "A. James Gosling",
            "B. Dennis Ritchie",
            "C. Guido van Rossum",
            "D. Elon Musk"
        ],
        "answer": "C"
    }
]

# Store the user's score.
score = 0

print("=" * 40)
print("🧠 PYTHON QUIZ GAME")
print("=" * 40)

# Loop through every question.
for question_data in questions:

    print(f"\n{question_data['question']}")

    # Display all answer choices.
    for option in question_data["options"]:
        print(option)

    # Read the user's answer.
    # upper() converts a, b, c, d into A, B, C, D.
    user_answer = input("Your Answer: ").strip().upper()

    # Compare the user's answer with the correct answer.
    if user_answer == question_data["answer"]:
        print("✅ Correct!")
        score += 1

    else:
        print(f"❌ Wrong! Correct answer: {question_data['answer']}")

# Display the final score.
print("\n" + "=" * 40)
print(f"🎉 Final Score : {score}/{len(questions)}")
print("=" * 40)

# Calculate the percentage.
percentage = (score / len(questions)) * 100

print(f"Percentage : {percentage:.2f}%")

# Display performance.
if percentage >= 80:
    print("🏆 Excellent!")

elif percentage >= 60:
    print("👍 Good Job!")

else:
    print("📚 Keep Practicing!")