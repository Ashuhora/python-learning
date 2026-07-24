# Importing the random module

import random

number = random.randint(1, 10)

print(number)

# Coin Flip example

import random

coin = random.randint(1, 2)

if coin == 1:
    print("Heads")
else:
    print("Tails")
