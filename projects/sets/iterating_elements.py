# iterating follows the same patterns as a for loop.
# Because sets are unordered, the order of the elements is not guaranteed.

colors = set(["red", "blue", "green"])
counter = 1
print("color lists")

for color in colors:
    print(f"{counter}. {color}")
    counter +=1