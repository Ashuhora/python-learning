import random


class Game:

    def __init__(self):
        # Initialize board with string numbers for easy selection
        self.board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.current_player = random.choice(["X", "O"])

    def change_player(self):
        """
        Switch the player mark.
        """
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    def is_valid_move(self, position: int) -> tuple[bool, str]:
        """
        Board must not be X or O and position must be in range.
        """
        if position < 1 or position > 9:
            return (False, "Invalid board position")

        index = position - 1

        if self.board[index] == "X" or self.board[index] == "O":
            return (False, "That spot is already taken")

        return (True, "Valid move")

    def place_mark(self, position: int) -> tuple[bool, str]:
        """
        Places the current player's mark.
        """
        index = position - 1

        self.board[index] = self.current_player

        if self.check_winner():
            return (True, f"{self.current_player} wins!")

        elif self._is_board_full():
            return (True, "The game is a draw!")

        self.change_player()

        return (False, f"It's {self.current_player}'s turn.")

    def check_winner(self) -> bool:
        """
        Check if the current player has won.
        """

        # Rows
        if self.board[0] == self.board[1] and self.board[1] == self.board[2]:
            return True

        if self.board[3] == self.board[4] and self.board[4] == self.board[5]:
            return True

        if self.board[6] == self.board[7] and self.board[7] == self.board[8]:
            return True

        # Columns
        if self.board[0] == self.board[3] and self.board[3] == self.board[6]:
            return True

        if self.board[1] == self.board[4] and self.board[4] == self.board[7]:
            return True

        if self.board[2] == self.board[5] and self.board[5] == self.board[8]:
            return True

        # Diagonals
        if self.board[0] == self.board[4] and self.board[4] == self.board[8]:
            return True

        if self.board[2] == self.board[4] and self.board[4] == self.board[6]:
            return True

        return False

    def _is_board_full(self) -> bool:
        """
        Check if the board is full.
        """
        for cell in self.board:
            if cell != "X" and cell != "O":
                return False

        return True