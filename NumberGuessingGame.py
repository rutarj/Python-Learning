# Summary of What You Learned While Writing This Code
# Random Number Generation:

# Used random.randint() to generate a random number.
# Conditional Statements:

# Handled different scenarios using if, elif, and else statements.
# User Input Handling:

# Collected and processed user input with input() and int().
# Function Design:

# Created a check_guess function to modularize guess checking logic.
# Loop Structures:

# Used a for loop to manage the number of attempts.
# String Interpolation:

# Used f-strings to include variables in strings for better output.
# Game Feedback:

# Provided feedback based on the user's guesses and attempts.
import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(1, 100)

def check_guess(user_guess, number):
    if user_guess == number:
        print(f"You got it! The answer was {number}.")
        return True
    elif user_guess > number:
        print("Too high.")
    else:
        print("Too low.")
    return False

p_choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
if p_choice == "easy":
    attempts = 10
elif p_choice == "hard":
    attempts = 5
else:
    print("Invalid choice. Defaulting to 'easy' mode.")
    attempts = 10

for attempt in range(attempts, 0, -1):
    print(f"You have {attempt} attempts remaining to guess the number.")
    user_chosen = int(input("Make a guess: "))

    if check_guess(user_chosen, number):
        break
    elif attempt == 1:
        print("You've run out of guesses, you lose.")
    else:
        print("Guess again.")
