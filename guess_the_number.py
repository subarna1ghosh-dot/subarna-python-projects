# -----------------------------------------------
# Mini-Project: Guess the Number Game
# Created by: Subarna Ghosh
# -----------------------------------------------

import random

secret_number = random.randint(1, 10)
print("Welcome to the Guess the Number Game!")

while True:
    try:
        guess = int(input("Guess a number between 1 and 10: "))
    except ValueError:
        print("Please enter a valid integer.")
        continue

    if guess < secret_number:
        print("Wrong Guess! Too low, try again.")
    elif guess > secret_number:
        print("Wrong Guess! Too high, try again.")
    else:
        print("Congratulations! You guessed it right.")
        break
