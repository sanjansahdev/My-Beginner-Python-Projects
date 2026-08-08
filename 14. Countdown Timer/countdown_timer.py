# ----------------------------------------------------------
# Program : Countdown Timer
# Author  : G. Sanjansah
# Purpose : Count down from a specified number of seconds
#           and display a message when the timer finishes.
# ----------------------------------------------------------

# Import the time module.
# It provides functions related to time and delays.
import time

# Read the countdown duration from the user.
seconds = int(input("Enter countdown time (seconds): "))

# Continue looping until the timer reaches zero.
while seconds > 0:

    # Display the remaining time.
    print(seconds)

    # Pause the program for 1 second.
    time.sleep(1)

    # Decrease the timer by 1 second.
    seconds -= 1

# Display a message after the countdown ends.
print("⏰ Time's Up!")