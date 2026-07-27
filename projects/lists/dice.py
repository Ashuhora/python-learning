# roling two dice multiple times and display how often each total appears.

import random

num_rolls = int(input("Enter the numbers of rolls: "))


results = [0] * 11

# roll the two dice the requested number of times.

for i in range(num_rolls):
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    results[roll1 + roll2 -2] += 1

print("roll\tcount\tpercent")


for i in range(len(results)):
    percent = results[i] / num_rolls

    print(f"{i + 2}\t{results[i]}\t{percent:.0%}")