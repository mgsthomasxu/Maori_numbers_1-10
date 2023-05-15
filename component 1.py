import random

# Define Maori numbers and their English translations
numbers = {
    "tahi": "one",
    "rua": "two",
    "toru": "three",
    "whā": "four",
    "rima": "five",
    "ono": "six",
    "whitu": "seven",
    "waru": "eight",
    "iwa": "nine",
    "tekau": "ten"
}

# Generate a random question
def generate_question():
    maori_number = random.choice(list(numbers.keys()))
    english_number = numbers[maori_number]
    return maori_number, english_number

# Check user's answer
def check_answer(question, answer):
    maori_number, english_number = question
    if answer.lower() == english_number:
        return True
    return False

# Main quiz loop
def quiz():
    score = 0
    total_questions = 10

    print("Welcome to the Maori Number Quiz!")
    print("Translate the Maori numbers into English.")

    for _ in range(total_questions):
        question = generate_question()
        maori_number, _ = question

        print("\nWhat is the English translation of '{}'?".format(maori_number))
        user_answer = input("Your answer: ")

        if check_answer(question, user_answer):
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is '{}'.".format(numbers[maori_number]))

    print("\nQuiz complete!")
    print("You scored {} out of {}.".format(score, total_questions))

# Run the quiz
quiz()