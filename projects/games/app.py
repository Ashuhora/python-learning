import os
from game import Game


def clear_screen():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Linux/Mac
    else:
        os.system('clear')


def print_instructions():
    clear_screen()
    print("Welcome to Tic Tac Toe!")
    print("Player 1: X, Player 2: O")
    print("Enter a number (1-9) to place your mark.")
    print("The positions are numbered as follows:")
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 ")
    print("\n")
    input("Press any key to start...")


def display_board(board: list[str]):
    """
    Prints the current state of the board in a grid format.
    """
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")


def prompt_play_again() -> bool:
    """
    Prompts the user for whether they want to play again.
    """
    return input("Would you like to play again (y/n)? ").lower() == "y"


def get_player_input(game: Game) -> int:
    """
    Gets a valid input from the user.
    """
    while True:
        try:
            position = int(input("Choose a position (1-9): "))
            is_valid, message = game.is_valid_move(position)

            if not is_valid:
                print(message)
            else:
                return position

        except:
            print("That is not a valid position!")


def main():
    """
    Main function to run the game.
    """
    print_instructions()

    play_again = True

    while play_again:
        game = Game()
        game_over = False

        while not game_over:
            clear_screen()
            display_board(game.board)

            print(f"It is {game.current_player}'s turn.")
            position = get_player_input(game)

            game_over, message = game.place_mark(position)
            print(message)

        display_board(game.board)

        play_again = prompt_play_again()


if __name__ == "__main__":
    main()