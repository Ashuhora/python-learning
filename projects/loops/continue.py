# This Prints only even numbers from 1 to 10.

counter = 0

while counter < 10:
    counter = counter + 1

    if counter % 2 == 1:
        continue

    print(counter)