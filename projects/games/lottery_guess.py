# This is a simple lottery guessing game.

import random

numbers = random.sample(range(1, 41), 6)
numbers.sort()

for number in numbers:
    print(f"{number:02d}")
