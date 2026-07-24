# This will Keep asking until the user enters a positive number.

while True:
     number = int(input("Enter a positive number: "))

     if number > 0:
        break

print("Thank you!")