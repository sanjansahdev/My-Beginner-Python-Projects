# ----------------------------------------------------------
# Program : Digital Clock
# Author  : G. Sanjansah
# Purpose : Display the current time and update it every
#           second like a digital clock.
# ----------------------------------------------------------

# Import the time module.
import time

# Keep the clock running continuously.
while True:

    # Get the current time in HH:MM:SS format.
    current_time = time.strftime("%H:%M:%S")

    # Display the current time.
    # end="\r" returns the cursor to the beginning of the line
    # so the next time replaces the previous one.
    print(current_time, end="\r")

    # Wait for one second before updating the clock.
    time.sleep(1)