# Day 3 - Number Guessing Game
print("#30 coding challenge")

import random

# Random number between 1 and 20
secret_number = random.randint(1, 20)
attempts = 0

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 20.")

while True:
    guess = input("Enter your guess: ")
    
    if not guess.isdigit():
        print("Please enter a valid number!")
        continue
    
    guess = int(guess)
    attempts += 1
    
    if guess < secret_number:
        print("Too low! 📉 Try again.")
    elif guess > secret_number:
        print("Too high! 📈 Try again.")
    else:
        print(f"🎉 Correct! The number was {secret_number}.")
        print(f"You guessed it in {attempts} attempts.")
        break
