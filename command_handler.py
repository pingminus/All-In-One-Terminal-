#command_handler.py
from logging import exception
from pickle import TUPLE1

from color_manager import ColorManager
from link_fetcher import LinkFetcher
from tic_tac_toe import TicTacToe
from key_logger import KeyLogger  # Import the KeyLogger class
from Timer import Timer

class CommandHandler:
    """Handle user input and commands."""

    def __init__(self):
        self.color_manager = ColorManager()
        self.key_logger = None  # Initialize the key logger as None
        self.hidden_key_logger = None  # For the hidden key logger
        self.timer = Timer()

    def wait_for_input(self):
        while True:
            user_input = input(
                f"{self.color_manager.current_color}user@host:~$ ")  # Prompt for user input with current color

            if user_input==("e"):  # Exit condition
                print(f"Exiting...")  # Color persists
                break
            elif self.isCalculation(user_input)==True and user_input.find('https:/')==-1:
                self.perform_Calculation(user_input)

            elif user_input.startswith("h"):
                self.display_help()
            elif user_input.startswith("i"):
                self.printName()
                print("This is a custom Terminal like application v.0.1.4")
                print("Just some small python projects combined in one")
                print("by https://github.com/pingminus")
            elif user_input=="t":
               self.timer.runTimer()
            elif user_input.startswith("u"):
                URL = user_input[1:].strip()  # Get the URL after 'u'
                self.fetch_links(URL)
            elif user_input.startswith("g"):
                self.handle_game_commands(user_input)
            elif user_input == "k hidden":
                self.start_hidden_key_logger()  # Start hidden key logger
            elif user_input == "k":
                self.start_normal_key_logger()  # Start normal key logger
            elif user_input.startswith("stopkeylogger"):
                self.stop_key_logger()  # Stop key logger
            elif user_input.startswith("color "):
                self.change_color(user_input)

    def display_help(self):
        """Display help commands."""
        print("")
        print("     -e              Exit                   -g              Games")
        print("     -u              LinkFetcher            -k              Start Key Logger")
        print("     -stopkeylogger  Stop Key Logger        -k hidden       hidden Key Logger")  # Help for stopping key logger
        print("     -color          Change Color           -t              Timer")
        print("       -list  Color List                    -i              Information")

    def fetch_links(self, URL):
        """Fetch and display links from a URL."""
        links = LinkFetcher.fetch(URL)
        for link in links:
            if link.startswith('http'):
                print(f"{link}")  # Print with current color
            else:
                print(f"{URL + link}")  # Print with current color

    def handle_game_commands(self, user_input):
        """Handle game commands like starting TicTacToe."""
        if user_input[1:].strip() == "":
            print(f"====GAMES====")
            print(f"TicTacToe")
        elif user_input[1:].strip().lower() in ["tictactoe", "t"]:
            game = TicTacToe()
            print("Exit Game with -1")
            game.play()
    def isCalculation(self, user_input):
        return any(op in user_input for op in ["/","*", "+", "-"])
    def perform_Calculation(self, user_input):
        try :
            result = eval(user_input)
            print(f"{result}")
        except Exception as e:
            print(f"Error:{e}")

    def start_hidden_key_logger(self):
        """Start the hidden key logger in a background thread."""
        if not self.hidden_key_logger:  # Check if no hidden key logger is running
            self.hidden_key_logger = KeyLogger()  # Create a new KeyLogger instance
            self.hidden_key_logger.start_hidden_logging()
        else:
            print(f"Hidden key logger is already running.")

    def start_normal_key_logger(self):
        """Start the normal key logger (visible key logging)."""
        if not self.key_logger:  # Check if no key logger is running
            self.key_logger = KeyLogger()  # Create a new KeyLogger instance
            self.key_logger.start_logging()
        else:
            print(f"Key logger is already running.")

    def stop_key_logger(self):
        """Stop the key logger (both normal and hidden)."""
        if self.key_logger:
            self.key_logger.stop_logging()  # Stop the normal key logger
            self.key_logger = None
        if self.hidden_key_logger:
            self.hidden_key_logger.stop_logging()  # Stop the hidden key logger
            self.hidden_key_logger = None
        else:
            print(f"{self.color_manager.current_color}No key logger is running.")


    def change_color(self, user_input):
        """Handle color changing commands."""
        colorList = [
            "green", "light_blue", "red", "yellow",
            "magenta", "cyan", "white", "black",
            "dark_green", "dark_blue", "dark_red",
            "dark_yellow", "light_magenta", "light_cyan"
        ]
        try:
        # Split the user input and check if the second part is in colorList
            color_command = user_input.split()[1]  # Get the color command
            if color_command.startswith("list"):
                for color in colorList:
                    print(f"{self.color_manager.current_color}{color}")
            elif color_command in colorList:  # Check if the color_command is valid
                self.color_manager.set_color(color_command)  # Set the color
            else:
                print(f"{self.color_manager.current_color}Invalid color! Please choose from: {', '.join(colorList)}")
        except Exception as e:
            print(f"Error: {e}")

    def printName(self):
        print("\033[38;2;255;0;0m" + "┌─┐┬┌┐┌┌─┐┌─┐┬  ┬ ┬┌─┐")  # Red
        print("\033[38;2;255;80;0m" + "├─┘│││││ ┬├─┘│  │ │└─┐")  # More orange
        print("\033[38;2;255;165;0m" + "┴  ┴┘└┘└─┘┴  ┴─┘└─┘└─┘")  # Full orange
        print("\033[0m")  # Reset terminal color
