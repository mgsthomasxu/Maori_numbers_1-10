"""Maori_N Yes/No Checker
based on 01_yes_no_v2"""


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


# Main routine go here...
show_instructions = yes_no("Have you played this game before?: ").lower()
print(f"You entered '{show_instructions}'")
print()
having_fun = yes_no("Are you having fun?: ").lower()
print(f"You entered '{having_fun}'")
