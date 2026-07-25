# This program finds all the factors of a number.

target= int(input("Enter a number to calculate the factors of: "))

for x in range(1, target + 1):
    if (target % x == 0):
        print(x)

# This is more efficient way to solve the problems.
# No factor can be > half the number, so we can stop.

target = int(input("Enter a number to calculate the factor of: "))

for x in range(1, target + 1):
    if (target % x == 0):
        print(x)


    if (x > target // 2):
         break

print(target)