"""Maori_N"""


# The functions go here...
def yes_no(question_text):
    while True:
        # Ask the user if they have played before
        answer = input(question_text).lower()

        # If they say yes, output 'Continue Game'
        if answer == 'yes' or answer == "y":
            answer = "Yes"
            return answer

        # If they say no, output 'Display instruction'
        elif answer == 'no' or answer == 'n':
            return answer

        # Other answers are error
        else:
            print("Please answer with 'Yes' or 'No'")


show_instructions = yes_no("Have you played this game before?: ").lower()
print(f"You entered '{show_instructions}'")
print()
having_fun = yes_no("Are you having fun?: ").lower()
print(f"You entered '{having_fun}'")

import random
from collections import deque

# Define Maori numbers from 1 to 10
numbers = {
    1: "tahi",
    2: "rua",
    3: "toru",
    4: "whā",
    5: "rima",
    6: "ono",
    7: "whitu",
    8: "waru",
    9: "iwa",
    10: "tekau"
}


# Function to generate a random question
def generate_question():
    num = random.randint(1, 10)
    maori_num = numbers[num]
    return num, maori_num


# Function to check the user's answer
def check_answer(user_answer, correct_answer):
    return user_answer.lower() == correct_answer


# Main quiz function
def quiz():
    score = 0
    num_questions = 10

    # Queue to hold the questions
    question_queue = deque()

    # Stack to hold the answers
    answer_stack = []

    # Generate the questions and answers
    for _ in range(num_questions):
        num, maori_num = generate_question()
        question_queue.append(f"What is the Maori word for {num}?")
        answer_stack.append(maori_num)

    while question_queue:
        question = question_queue.popleft()
        answer = answer_stack.pop()

        print(question)
        user_answer = input("Your answer: ")

        if check_answer(user_answer, answer):
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {answer}.")

        print("--------------------")

    print(f"Quiz complete! Your score: {score} / {num_questions}")


# Run the quiz
quiz()
