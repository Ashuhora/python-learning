# Path helps us work with file and folder locations
from pathlib import Path

# timezone lets us use UTC time
from datetime import datetime, timezone


class LogManager:
    """
    Manages application logging to a text file.
    """

    def __init__(self, log_path="data/log.txt"):
        # Convert the log file location into a Path object
        self.path = Path(log_path)

        # Create the data folder if it does not already exist
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def write(self, message: str) -> bool:
        """
        Write a message to the log file with a timestamp.

        Args:
            message (str): The message to log

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # isoformat() converts it into a standard text format
            timestamp = datetime.now(timezone.utc).isoformat()

            # Combine the timestamp and message into one log entry
            # \n moves the next log entry to a new line
            log_entry = f"[{timestamp}] {message}\n"

            # Open the log file in append mode
            # UTF-8 supports different letters, languages, and symbols
            with self.path.open("a", encoding="utf-8") as file:
                file.write(log_entry)

            # Return True to show that the log was saved correctly
            return True

        except Exception as e:
            # Display the error if the log file cannot be written
            print(f"Error writing to log: {e}")

            # Return False to show that writing failed
            return False

    def clear_log(self) -> bool:
        """
        Clears all information from the log file.
        """
        try:
            # Open the log file in write mode to erase its contents
            with self.path.open("w", encoding="utf-8"):
                pass

            return True

        except Exception as e:
            print(f"Error clearing log: {e}")
            return False

