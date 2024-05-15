# Hangman Game:

# The code initializes a list called stages, each element containing a hangman ASCII art representing a stage of the game.
# It sets up variables for the game, such as end_of_game, word_list, chosen_word, lives, and display.
# A while loop runs until end_of_game becomes true.
# Inside the loop, the user inputs a letter guess, and the program checks if it's in the chosen word.
# If the guess is incorrect, the player loses a life. If lives reach zero, the game ends with a "You lose" message.
# After each guess, the program prints the current state of the word using underscores for unrevealed letters.
# If all letters are guessed correctly, the game ends with a "You win" message.
# ASCII art corresponding to the current number of lives is printed at each iteration.

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6

print(f'Pssst, the solution is {chosen_word}.')

display = ["_" for _ in range(word_length)]

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(' '.join(display))

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
