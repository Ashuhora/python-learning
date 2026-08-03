from pathlib import Path

# json helps us read and write JSON data
import json
class UserManager:
    """
    Handles loading, saving, creating, and logging in users.
    """

    def __init__(self, log_manager):
        # set the location of the users json file
        self.path = Path("data/users.json")

        # create the data folder if it does not exist
        self.path.parent.mkdir(parents=True, exist_ok=True)

        # Store the LogManager object for writing log messages
        self.log_manager = log_manager

        # start with an empty list of users
        self.users = []

        # Load existing users from users.json
        self._load()

    def _load(self):
        """
        Loads user data from the json file.
        """

        # stop if users.json does not exist
        if not self.path.exists():
            return

        try:
            # open users.json in read mode
            with self.path.open("r", encoding="utf-8") as file:
                # Convert json data into a Python list
                self.users = json.load(file)

        except Exception as e:
            # Record any file-loading error in log.txt
            self.log_manager.write(f"Error loading user data: {e}")

    def _save(self) -> bool:
        """
        Saves user data to the json file.

        Returns:
            bool: True if successful, False otherwise.
        """
        try:
            # Open users.json in write mode
            with self.path.open("w", encoding="utf-8") as file:
                # Save the users list as formatted JSON
                json.dump(self.users, file, indent=4)

            return True

        except Exception as e:
            # Record any file-saving error in log.txt
            self.log_manager.write(f"Error saving user data: {e}")
            return False

    def user_exists(self, user_name: str) -> bool:
        """
        Checks whether the username already exists.
        """

        # check each user dictionary in the users list
        for user in self.users:
            if user["user_name"] == user_name:
                return True

        return False

    def add_user(
        self,
        user_name: str,
        pin: str,
        is_admin: bool = False
    ) -> tuple[bool, str, dict]:
        """
        Adds a new user.
        """

        # Prevent duplicate usernames
        if self.user_exists(user_name):
            return (
                False,
                f"The user: {user_name} already exists!",
                None
            )

        try:
            # create the new user dictionary
            user = {
                "user_name": user_name,
                "pin": pin,
                "is_admin": is_admin
            }

            # Add new user to the list
            self.users.append(user)

            # save the updated user list
            if not self._save():
                # Remove the user from memory if saving failed
                self.users.remove(user)

                return (
                    False,
                    "The user could not be saved.",
                    None
                )

            # Record the successful registration
            self.log_manager.write(f"User {user_name} created.")

            return (
                True,
                "User record created!",
                user
            )

        except Exception as e:
            return (
                False,
                f"The user could not be added: {e}",
                None
            )

    def login(self, user_name: str, pin: str) -> dict:
        """
        Attempts to log in a user.
        """

        # Search for a matching username and PIN
        for user in self.users:
            if (
                user["user_name"] == user_name
                and user["pin"] == pin
            ):
                # Record the successful login
                self.log_manager.write(
                    f"User {user_name} logged in."
                )
                return user

        # Record the failed login attempt
        self.log_manager.write(
            f"Failed login attempt for {user_name}"
        )

        return None


