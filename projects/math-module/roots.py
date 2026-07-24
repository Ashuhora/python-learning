# This is Square Root Calculator

import math

# Ask the user for a number

number = float(input("Enter a number:"))

# Check if the number is positive

if number >= 0:
    square_root = math.sqrt(number)
    print(f"Square root is: {square_root}")
else:
    print("Error: Cannot calculate the square root of a negative number")
