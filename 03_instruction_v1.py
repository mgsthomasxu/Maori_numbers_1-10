import random

# Define Maori numbers and their corresponding English translations
numbers = {
    0: "kore",
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

# Generate a random Maori number
random_number = random.randint(0, 10)

# Get the English translation of the Maori number
english_translation = numbers[random_number]

# Prompt the user to guess the Maori number
guess = input("Guess the Maori number (0-10): ")

# Check if the guess is correct
if guess.isdigit() and int(guess) in numbers:
    if int(guess) == random_number:
        print("Correct!")
    else:
        print("Incorrect! The correct answer is:", numbers[random_number])
else:
    print("Invalid input. Please enter a number from 0 to 10.")
