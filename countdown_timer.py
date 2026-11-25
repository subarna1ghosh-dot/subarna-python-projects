# -----------------------------------------------
# Mini-Project: Countdown Timer
# Created by: Subarna Ghosh
# -----------------------------------------------

import time

print("Welcome to the Python Countdown Timer!")

while True:
    try:
        seconds = int(input("Enter countdown time in seconds: "))
        if seconds <= 0:
            print("Please enter a positive number greater than 0.")
            continue
        break
    except ValueError:
        print("Invalid input! Please enter a whole number.")

print("\nStarting countdown...")
for remaining in range(seconds, 0, -1):
    mins, secs = divmod(remaining, 60)
    print(f"Time remaining: {mins:02d}:{secs:02d}", end="\r")
    time.sleep(1)

print("\nTime's up! Countdown complete.")

