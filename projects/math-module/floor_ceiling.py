# Floor and Celing

import math

# Ask the user for a decimal number

number = float(input("Enter a decimal number " ))

# Calculate the floor and ceiling

floor_number = math.floor(number)
ceiling_number = math.ceil(number)

# Display the results

print(f"Floor:{floor_number}")
print(f"Ceiling: {ceiling_number}")