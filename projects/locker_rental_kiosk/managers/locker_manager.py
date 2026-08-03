from pathlib import Path
import json
from datetime import datetime, timezone

class LockerManager:
    """
    Manages the lockers in the rental kiosk.
    """
    def __init__(self, log_manager, capacity=20):
        # File that stores locker data
        self.path = Path("data/lockers.json")

        # Used to write messages to the log file
        self.log_manager = log_manager
        self.capacity = capacity

        # Stores all locker data
        self.lockers = {}

        # Create empty lockers
        self._initialize_lockers()

        # Load saved locker data
        self._load()

    def _initialize_lockers(self):
        # Create locker numbers from 1 to the capacity
        for locker_num in range(1, self.capacity + 1):
            # None means the locker is empty
            self.lockers[str(locker_num)] = None

    def _load(self):
        # If the file does not exist, save the new empty lockers
        if not self.path.exists():
            self._save()
            return
        try:
            # Open the file and load the saved locker data
            with self.path.open("r") as file:
                saved_lockers = json.load(file)

            # Use the saved data if it contains lockers
            if saved_lockers:
                self.lockers = saved_lockers

            # If the file is empty, save the initialized lockers
            else:
                self._save()

        except Exception as e:
            self.log_manager.write(
                f"Error loading locker data: {e}"
            )

    def _save(self):
        # Save locker data to lockers.json
        try:
            # Open the file for writing
            with self.path.open("w") as file:
                # Save the locker dictionary as JSON
                json.dump(self.lockers, file, indent=4)

            # Saving worked
            return True

        except Exception as e:
            # Write an error message to the log
            self.log_manager.write(
                f"Error saving locker data: {e}"
            )

            # Saving failed
            return False

    def is_locker_available(self, locker_number: str) -> bool:
        # Check if the locker number exists
        if locker_number not in self.lockers:
            return False

        if self.lockers[locker_number] is None:
            return True

        # The locker is occupied
        return False

    def add_rental(
        self,
        user_name: str,
        contents: str,
        locker_number: str
    ) -> tuple[bool, str]:

        # Check if the locker number exists
        if locker_number not in self.lockers:
            message = f"Invalid locker number: {locker_number}"
            return False, message

        # Check if the locker is already rented
        if not self.is_locker_available(locker_number):
            message = f"Locker {locker_number} is already occupied"
            return False, message

        # Create the rental information
        rental = {
            # Name of the person renting the locker
            "user_name": user_name,

            # Current date and time in UTC
            "rental_date": datetime.now(
                timezone.utc
            ).isoformat(),

            # Items stored inside the locker
            "contents": contents
        }

        # Put the rental information in the locker
        self.lockers[locker_number] = rental

        # Save the new rental
        if self._save():
            message = (
                f"Locker {locker_number} rented to "
                f"{user_name}"
            )

            # Write the rental message to the log
            self.log_manager.write(message)
            return True, message

        # Return this message if saving fails
        return False, "Failed to save locker rental"

    def end_rental(
        self,
        locker_number: str
    ) -> tuple[bool, str]:

        # Check if the locker number exists
        if locker_number not in self.lockers:
            message = f"Invalid locker number: {locker_number}"
            return False, message

        if self.lockers[locker_number] is None:
            message = (
                f"Locker {locker_number} is already vacant"
            )
            return False, message

        # Remove the rental information
        self.lockers[locker_number] = None

        # Save the empty locker
        if self._save():
            message = f"Locker {locker_number} vacated."

            # Write the message to the log
            self.log_manager.write(message)

            return True, message

        # Return this message if saving fails
        return False, "Failed to save locker vacancy"

    def get_all_rentals(self) -> dict:
        # Store all occupied lockers
        rentals = {}

        # Check every locker
        for locker_num, rental in self.lockers.items():
            # Add only occupied lockers
            if rental is not None:
                rentals[locker_num] = rental

        return rentals

    def get_user_rentals(self, user_name: str) -> dict:
        # Store rentals for one user
        user_rentals = {}

        # Check every locker
        for locker_num, rental in self.lockers.items():
            # Check if the locker belongs to this user
            if (
                rental is not None
                and rental["user_name"] == user_name
            ):
                user_rentals[locker_num] = rental

        return user_rentals

    def get_available_lockers(self) -> list[str]:
        # Store all empty locker numbers
        available_lockers = []
        
        for locker_num, rental in self.lockers.items():
            # Add lockers that are empty
            if rental is None:
                available_lockers.append(locker_num)

        return available_lockers






