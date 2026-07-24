# The user enters numbers until they type Q to quit.

total = 0
user_input = ""

while user_input != "Q":
    user_input = input("Enter a number (Q to quit): ").upper()

    if user_input != "Q":
        total += int(user_input)

print(f"\nThe total is: {total}")