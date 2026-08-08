# ----------------------------------------------------------
# Program : Rock Paper Scissors Game
# Author  : G. Sanjansah
# Purpose : Play Rock, Paper, Scissors against the computer.
# ----------------------------------------------------------

# Import the random module to let the computer make a random choice.
import random

# Store all valid choices in a list.
choices = ["rock", "paper", "scissors"]

print("=" * 40)
print("🎮 ROCK PAPER SCISSORS")
print("=" * 40)

# Keep the game running until the user chooses to quit.
while True:

    # Ask the user for their choice.
    # lower() converts the input to lowercase so that
    # "Rock", "ROCK", and "rock" are treated the same.
    user = input("\nChoose Rock, Paper, or Scissors: ").lower()

    # Check whether the entered choice is valid.
    if user not in choices:
        print("❌ Invalid choice! Please choose Rock, Paper, or Scissors.")
        continue

    # Let the computer randomly select one option.
    computer = random.choice(choices)

    # Display both choices.
    print(f"\n🧑 You chose      : {user}")
    print(f"💻 Computer chose : {computer}")

    # Decide the winner.
    if user == computer:
        print("🤝 It's a Tie!")

    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        print("🎉 You Win!")

    else:
        print("😢 Computer Wins!")

    # Ask whether the player wants another round.
    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    # Exit the game if the answer is not "yes".
    if play_again != "yes":
        print("\n👋 Thanks for playing!")
        break