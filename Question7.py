# Define the quiz questions
questions = [
    {
        "question": "What is the output of `print(2 ** 3)`?",
        "options": ["A. 6", "B. 8", "C. 9", "D. 12"],
        "answer": "B"
    },
    {
        "question": "Which of the following is used to define a function in Python?",
        "options": ["A. func", "B. define", "C. def", "D. function"],
        "answer": "C"
    },
    {
        "question": "What does the `len()` function do?",
        "options": ["A. Returns the type of an object", "B. Returns the length of an object", "C. Converts a string to lowercase", "D. None of the above"],
        "answer": "B"
    },
    {
        "question": "Which of the following is NOT a Python data type?",
        "options": ["A. int", "B. float", "C. string", "D. array"],
        "answer": "D"
    },
    {
        "question": "What is the correct way to create a list in Python?",
        "options": ["A. {1, 2, 3}", "B. [1, 2, 3]", "C. (1, 2, 3)", "D. <1, 2, 3>"],
        "answer": "B"
    }
]


def run_quiz(questions):
    score = 0
    for i, question in enumerate(questions):
        print(f"\nQuestion {i + 1}: {question['question']}")
        for option in question["options"]:
            print(option)
        user_answer = input("Your answer (A/B/C/D): ").upper()
        if user_answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {question['answer']}.")
    return score


def display_result(score, total_questions):
    print(f"\nQuiz over! You scored {score} out of {total_questions}.")
    if score == total_questions:
        print("Perfect score! You're a Python expert!")
    elif score >= total_questions // 2:
        print("Good job! You know your Python basics.")
    else:
        print("You need more practice. Keep learning!")


print("Welcome to the Python Quiz Game!")
print("Answer the following questions to test your Python knowledge.\n")

total_questions = len(questions)
final_score = run_quiz(questions)
display_result(final_score, total_questions)