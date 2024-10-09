# tic_tac_toe.py

class TicTacToe:
    """Tic Tac Toe game logic."""

    def __init__(self, color_manager):
        self.color_manager = color_manager
        self.board = [['■', '■', '■'],
                      ['■', '■', '■'],
                      ['■', '■', '■']]
        self.count = 0

    def print_board(self):
        print(f"{self.color_manager.current_color}{'-' * 5}")
        for row in self.board:
            for cell in row:
                print(f"{self.color_manager.current_color}{cell}", end=' ')  # Print each cell in current color
            print()  # Move to the next line after printing each row
        print(f"{self.color_manager.current_color}{'-' * 5}")  # Print a separator in current color

    def OnExit(self,user_row,user_column):
        if user_row == -1 or user_column == -1:
            print(f"{self.color_manager.current_color}Exiting TicTacToe...")
            return True
        return False

    def play(self):
        self.print_board()
        while True:
            try:
                print(f"{self.color_manager.current_color}What is your move? Provide row and column number (0, 1, 2).")
                user_row = int(input(f"{self.color_manager.current_color}Row >> "))
                if self.OnExit(user_row,0) == True:
                    return  # Check exit after getting row

                user_column = int(input(f"{self.color_manager.current_color}Column >> "))
                if self.OnExit(user_row, user_column) == True:
                    return  # Check exit after getting column

                # Validate input
                if user_row < 0 or user_row >= 3 or user_column < 0 or user_column >= 3:
                    print(f"{self.color_manager.current_color}Invalid input. Row and column must be between 0 and 2.")
                    continue

                # Check if the selected cell is already taken
                if self.board[user_row][user_column] != '■':
                    print(f"{self.color_manager.current_color}Cell is already occupied! Try again.")
                    continue

            except ValueError:
                print(f"{self.color_manager.current_color}Invalid input. Please enter integers for row and column.")
                continue  # Prompt again for valid input

            # Mark the board for the current player (X or O)
            if self.count % 2 == 0:
                self.board[user_row][user_column] = 'X'  # Player 1's move
            else:
                self.board[user_row][user_column] = 'O'  # Player 2's move

            self.print_board()
            self.count += 1
