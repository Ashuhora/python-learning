"""
Terminal input and output functions for the locker rental kiosk.
"""

import os 
from datetime import datetime

def clear_screen():
    """
    clears the terminal screen.
    """
    os.system("cls" if os.name == "nt" else "clear")

def wait_enter():
    """
    pause the program untill the user press Enter.
    """
    input("\nPress Enter to continue")

def get_user_name(
        prompt: str = "Enter username: ",
        min_length: int = 4,
        max_length: int = 20
) -> str:
        """
        get a valid username from the user.
        """
        while True:
             user_name = input(prompt).strip().lower()

             if not user_name:
                  print("Username cannot be blank.")
                  continue

             if len(user_name) < min_length:
                  print(f"Username must have at least "
                        f"{min_length} characters."
                )
                  continue
             if len(user_name) > max_length:
                  print(
                       f"Username cannnot have more than "
                       f"{max_length} characters." 
                  )
                  continue
             return user_name

def get_pin() -> str:
     """
     gets a valid PIN containing 4 to 6 digits.
     """
     while True:
          pin = input("Enter a PIN (4 to 6 digits):").strip()

          if len(pin) < 4 or len(pin) > 6:
               print("PIN must contain 4 to 6 digits.")
               continue
          if not pin.isdigit():
               print("PIN must only contain numbers.")
               continue

          return pin

def get_number_from_list(title: str, numbers: list[str]) -> str:
     """
     diaplays valid locker numbers and gets one choice.
     """
     # be sure every locker number is a string
     valid_numbers = [str(number) for number in numbers]
     print(title)
     print(", ".join(valid_numbers))

     while True:
          locker_number = input("Enter locker number: ").strip()

          if locker_number in valid_numbers:
               return locker_number

          print("That is not a valid locker number.")

def get_contents() -> str:
     """
     get information of the locker contents.
     """
     while True:
          contents = input("Waht are you storing in the locker?").strip()

          if contents:
               return contents

          print ("contents cannot be blank.")

def get_menu_choice(prompt: str, valid_choice: list[str]) -> str:
     """
     get a valid menu choice from the user
     """
     while True:
          choice = input(prompt).strip()

          if choice in valid_choice:
               return choice

          print("That is not a valid choice. Try again.")

def main_menu() -> str:
     """
     Displays the main locker kiosk menu.
     """
     clear_screen()

     print("Locker Rental Kiosk")
     print("_" * 50)
     print("1. Log In")
     print("2. Register")
     print("3. Quit")
     print()

     return get_menu_choice("Enter choice (1-3): ", ["1", "2", "3"])

def display_lockers(lockers: dict):
     """
     Display locker rental information in a table.
     """

     print("\nLocker Information")
     print("_" *80)

     if not lockers:
          print("No lockers are currently rented.")
          return

     print(
          f"{'Number':<10}"
          f"{'User':<20}"
          f"{'Date':<20}"
          f"{'Contents'}"
     )

     print("_" * 80)

     for locker_number, rental_info in lockers.items():
          user_name = rental_info.get("user_name", "Unknown")

          rental_date = rental_info.get("rental_date", "")

          contents = rental_info.get("contents", "")

          try:
               date_text = datetime.fromisoformat(rental_date).strftime("%m-%d-%Y %H:%M")

          except (ValueError, TypeError):
               date_text = rental_date or "Unknown"

          short_contents = contents[:25]

          print(
               f"{str(locker_number):<10}"
               f"{user_name:<20}"
               f"{date_text:<20}"
               f"{short_contents}"

          )



          
          



