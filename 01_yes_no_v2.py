"""Maori_N Yes/No Checker
Put the code created in v1 into loop to make the test easier"""

show_instruction = ""
while show_instruction != "x":

    # Ask the user if they have played before
    show_instruction = input("Have you played this game before?: ").lower()

    # If they say yes, output 'Continue Game'
    if show_instruction == 'yes' or show_instruction == 'y':
        print("Continue Game")

    # If they say no, output 'Display instruction'
    elif show_instruction == 'no' or show_instruction == 'n':
        print("Display instruction")

    # Other answers are error
    else:
        print("Please answer with 'Yes' or 'No'")

    print(f"You entered '{show_instruction}'")
