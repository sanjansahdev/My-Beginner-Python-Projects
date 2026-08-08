# ----------------------------------------------------------
# Program : Number Guessing Game
# Author  : G. Sanjansah
# Purpose : Guess a randomly generated number.
# ----------------------------------------------------------

# Import the random module.
# It allows Python to generate random numbers.
import random

# Generate a random integer between 1 and 100 (inclusive).
secret_number = random.randint(1, 100)

# Store the number of attempts made by the user.
attempts = 0

print("=" * 45)
print(" Welcome to the Number Guessing Game!")
print(" Guess a number between 1 and 100")
print("=" * 45)

# Keep asking until the correct number is guessed.
while True:

    # Ask the user to enter a number.
    guess = int(input("\n Enter your guess: "))

    # Increase the attempt counter.
    attempts += 1

    # Compare the user's guess with the secret number.
    if guess < secret_number:
        print("\n Too low! Try again.")

    elif guess > secret_number:
        print("\n Too high! Try again.")

    else:
        print("\n Congratulations!")
        print(f"\n You guessed the correct number: {secret_number}")
        print(f"\n Attempts taken: {attempts}")
        break   # Exit the loop because the correct answer was found.