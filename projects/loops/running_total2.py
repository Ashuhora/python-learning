
total = 0
user_input = ""

while True:
    user_input = input("Enter a number (Q to quit): ").upper()

    if user_input == "Q":
        break

    number = int(user_input)

    if number < 0:
        continue

    total += number

print(f"\nThe total is: {total}")