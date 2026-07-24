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

# Multiple Modules

import random
import math

print(random.randint(1, 6))
print(math.sqrt(64))

# Module Alias
# as gives the module a shorter name.

import random as rng

print(rng.randint(1, 10))

# Importing only One Function

from random import randint

print(randint(1, 10))

# Random Decimal
# This random() returns a decimal between 0.00 <= 1 (1 is not included)

import random

print(random.random())