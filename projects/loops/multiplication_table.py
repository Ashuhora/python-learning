# This prints a multiplication table.

for x in range(1, 6):
    print(f"\t{x}", end="")

print()

for row in range(1, 6):
    print(f"{row}\t", end="")

    for col in range(1, 6):
        print(f"{row * col}\t", end="")

    print()

# This program asks the user for a minimum and maximum value,
# then prints a multiplication table using nested for loops.

min = int(input("Enter the min value: "))
max = int(input("Enter the max value: "))

max += 1

# Print the column headings.

for x in range(min, max):
    print(f"\t{x}", end="")

print()

# Print each row.

for row in range(min, max):
    print(f"{row}\t", end="")

    # Print each column value.
    
    for col in range(min, max):
        print(f"{row * col}\t", end="")

    print()