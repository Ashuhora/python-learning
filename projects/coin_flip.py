import random

guess = input("(H)eads or (T)ails? ").upper()

num = random.randint(1, 2)

print("Flipping the coin...")

if num ==1:
    print("The coin landed on Heads!")
    
    if guess == "H":
        print("You guessed correctly!")
    else:
        print("You guessed wrong! try again!")


else:
    print("The coin landed on Tails!")

    if guess =="T":
        print("You guessed correctly!")
    else:
        print("You guessed wrong! Try again!")
