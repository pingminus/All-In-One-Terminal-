# tic_tac_toe.py
from itertools import count


class TicTacToe:
    """Tic Tac Toe game logic."""

    def __init__(self):

        self.board = [['■', '■', '■'],
                      ['■', '■', '■'],
                      ['■', '■', '■']]
        self.count = 0

    def print_board(self):
        print(f"{'-' * 5}")
        for row in self.board:
            for cell in row:
                print(f"{cell}", end=' ')  # Print each cell in current color
            print()  # Move to the next line after printing each row
        print(f"{'-' * 5}")  # Print a separator in current color

    def OnExit(self,user_row,user_column):
        if user_row == -1 or user_column == -1:
            print(f"Exiting TicTacToe...")
            return True
        return False

    def play(self):
        self.print_board()
        while True:
            try:
                print(f"What is your move? Provide row and column number (0, 1, 2).")
                user_row = int(input(f"Row >> "))
                if self.OnExit(user_row,0) == True:
                    return  # Check exit after getting row

                user_column = int(input(f"Column >> "))
                if self.OnExit(user_row, user_column) == True:
                    return  # Check exit after getting column

                # Validate input
                if user_row < 0 or user_row >= 3 or user_column < 0 or user_column >= 3:
                    print(f"Invalid input. Row and column must be between 0 and 2.")
                    continue

                # Check if the selected cell is already taken
                if self.board[user_row][user_column] != '■':
                    print(f"Cell is already occupied! Try again.")
                    continue

            except ValueError:
                print(f"Invalid input. Please enter integers for row and column.")
                continue  # Prompt again for valid input

            # Mark the board for the current player (X or O)
            if self.count % 2 == 0:
                self.board[user_row][user_column] = 'X'  # Player 1's move
            else:
                self.board[user_row][user_column] = 'O'  # Player 2's move

            self.print_board()

            # Check if the current player won
            if self.CheckWin():
                return  # Exit the game after a win

            # Check if it's a draw (no empty cells and no winner)
            if self.CheckDraw():
                return  # Exit the game after a draw

            # Increment the move counter after a valid move
            self.count += 1

    def CheckWin(self):
        #Check all win conditions

        #horizontal and vertical wins
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] and self.board[row][0] != '■':
                print("Congrats! You won!")
                return True
        for col in range(3):
           if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] != "■":
               print("Congrats! You won!")
               return True

        #Diagnoal wins
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != '■':
            print("Congrats! You won!")
            return True

        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != '■':
            print("Congrats! You won!")
            return True

        return False

    def CheckDraw(self):
            # Check if there are any empty cells left
        for row in self.board:
            if '■' in row:
                return False  # Not a draw if there's at least one empty cell

        print("It's a draw!")
        return True





