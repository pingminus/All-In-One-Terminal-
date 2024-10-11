# color_manager.py

from logging import exception

# ANSI escape codes for colors
COLOR_CODES = {
    'green': "\033[92m",
    'light_blue': "\033[94m",
    'red': "\033[91m",
    'yellow': "\033[93m",
    'magenta': "\033[95m",
    'cyan': "\033[96m",
    'white': "\033[97m",
    'black': "\033[90m",
    'dark_green': "\033[32m",
    'dark_blue': "\033[34m",
    'dark_red': "\033[31m",
    'dark_yellow': "\033[33m",
    'light_magenta': "\033[35m",
    'light_cyan': "\033[36m",
}

class ColorManager:
    """Manage the current text color."""

    def __init__(self):
        self.current_color = COLOR_CODES['green']  # Default color

    def set_color(self, color_command):
        """Set the current color based on the command."""
        try:
            self.current_color = COLOR_CODES.get(color_command, self.current_color)  # Default to current color if invalid
        except exception as e:
            print(f"{e}")
