# Circle Calculator

import math

# Ask the user to the circle radius

radius = float(input("Enter circle radius: "))

# Calculate the circumference and area

circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

# Display the result

print(f"The Circumference is: {circumference:.2f}")
print(f"The Area is: {area:.2f}")