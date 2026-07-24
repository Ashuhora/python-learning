# This is angle calculator

import math

# Ask the user for an angle number in degree

degrees = float(input("Enter an angle in degrees: "))

# convert degree to radians

radians = math.radians(degrees)

# Calculate the sine and cosine

sine = math.sin(radians)
cosine = math.cos(radians)

print(f"Sine: {sine:.4f}")
print(f"Cosine: {cosine:.4f}")