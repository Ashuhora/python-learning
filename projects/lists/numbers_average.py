# This creates an empty list and keeps asking the user
# for a number it stops when the user enters Q and 
# calculates the sum and avarage.

numbers = []

while True:
    user_input = input("Enter a number or Q to quit: ")

    if user_input == "Q":
        break

    numbers.append(int(user_input))

total = 0
for num in numbers:
    total += num

print(f"The sum of your numbers is {total}")
print(f"The average of your numbers is {total / len(numbers)}")