import random

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
    if user_answer.lower() == correct_answer:
        return True
    return False

# Main quiz function
def quiz():
    score = 0
    for _ in range(10):  # Ask 10 questions
        num, maori_num = generate_question()
        print(f"What is the Maori word for {num}?")
        user_answer = input("Your answer: ")
        if check_answer(user_answer, maori_num):
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {maori_num}.")
        print("--------------------")
    print(f"Quiz complete! Your score: {score}/10")

# Run the quiz
quiz()
