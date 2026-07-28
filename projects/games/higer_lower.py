# Import the random module

import random

# Get two random numbers between 1 and 10

num1 = random.randint(1, 10)
num2 = random.randint(1, 10)

# Display the first number

print(f"The first number is {num1}.")

# ask the player for a guess
guess = input("will the next number be (h)iger or (l)ower? ")

# Display the second number
print(f"The second number is {num2}.")

# Check if the player's guess is correct

if guess == "h" and num2 > num1:
    print("Correct!")
elif guess == "l" and num2 < num1:
    print("you guessed Correctly!")
else:
    print("sorry, you were wrong.")