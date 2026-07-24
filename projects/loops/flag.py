# Using Boolean variable to control the loop.

valid = False

while not valid:
    number = int(input("Enter a positive number: "))

    if number > 0:
        valid = True

print("Thank you!")