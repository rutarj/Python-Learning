# Rock, Paper, Scissors Game:

# The game starts by defining ASCII art representations for each choice: Rock, Paper, and Scissors.
# It prompts the user to input their choice: 0 for Rock, 1 for Paper, or 2 for Scissors.
# ASCII art corresponding to the user's choice is printed.
# The computer's choice is generated randomly between 0 and 2, and its corresponding ASCII art is printed.
# The winner is determined based on the choices and printed to the console.

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

print(f"user_choice {user_choice}")
if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
else:
    print(scissors)

computer_choice = random.randint(0,2)
print(f"Computer choice {computer_choice}")
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
else:
    print(scissors)

if computer_choice == user_choice:
    print("It's a draw")

elif computer_choice == 0 and user_choice == 1:
    print("You win")
elif computer_choice == 0 and user_choice == 2:
    print("You lose")
elif computer_choice == 1 and user_choice == 0:
    print("You lose")
elif computer_choice == 1 and user_choice == 2:
    print("You win")
elif computer_choice == 2 and user_choice == 0:
    print("You win")
elif computer_choice == 2 and user_choice == 1:
    print("You lose")
else:
    print("You typed an invalid number, you lose!")


