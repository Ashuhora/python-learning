# this let's the user guess a random number.
import random

# Defaults
max_value = 20
play_again = "y"

print("\nWelcome to the Number Guessing Game!")

# we will exit if they enter anything other than 'y'
while play_again.lower() == "y":
    while True:
        max_value = int(input("\nEnter the maximum value for your guessing range: "))
        if max_value <= 0:
            print("Please enter a positive number greater than 0.")
        else:
            break
    
    # Initialize the game
    secret_number = random.randint(1, max_value)
    guesses = set()
    
    print(f"I'm thinking of a number between 1 and {max_value}.")
    
    # Guessing loop
    while True:
        # Get user's guess

        guess = int(input("\nEnter your guess: "))
        
        # Check if guess is within range
        if guess < 1 or guess > max_value:
            print(f"Your guess must be between 1 and {max_value}.")
            continue
            
        # Check if guess is a duplicate
        if guess in guesses:
            print(f"You've already guessed {guess}. Try a different number.")
            continue
            
        # Add the valid guess to the set
        guesses.add(guess)

            
        # Check the guess against the secret number
        if guess < secret_number:
            print("Higher!")
        elif guess > secret_number:
            print("Lower!")
        else:
            print("You got it!")
            print(f"You found the number in {len(guesses)} guesses.")
            break
    
    # Ask if the user wants to play again
    play_again = input("\nWould you like to play again? (y/n): ")

print("\nThanks for playing! Goodbye!")