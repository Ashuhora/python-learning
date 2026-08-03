"""
User workflow functions for the locker rental kiosk.
"""
from workflows import terminal_io as io
from managers.locker_manager import LockerManager

def start_workflow(user: dict, locker_manager: LockerManager):
    """
    Runs the menu for a regular user.
    """
    while True:
        choice = user_menu()

        if choice == "1":
            view_rentals(user, locker_manager)

        elif choice == "2":
            add_rental(user, locker_manager)

        elif choice == "3":
            end_rental(user, locker_manager)

        elif choice == "4":
            print(
                f"\nLogging out. Have a great day, "
                f"{user['user_name']}!"
            )
            return


def user_menu() -> str:
    """
    Displays the menu for a regular user.
    """

    io.clear_screen()

    print("Locker Rental Kiosk")
    print("-" * 50)
    print("1. View Rentals")
    print("2. Rent Locker")
    print("3. End Rental")
    print("4. Log Out")
    print()

    return io.get_menu_choice(
        "Enter choice (1-4): ",
        ["1", "2", "3", "4"]
    )


def view_rentals(user: dict, locker_manager: LockerManager):
    """
    Displays the current user's locker rentals.
    """

    io.clear_screen()

    rentals = locker_manager.get_user_rentals(user["user_name"])

    if not rentals:
        print("You have no lockers rented.")
    else:
        io.display_lockers(rentals)

    io.wait_enter()


def add_rental(user: dict, locker_manager: LockerManager):
    """
    Allows the current user to rent a locker.
    """

    io.clear_screen()

    available_numbers = locker_manager.get_available_lockers()

    if not available_numbers:
        print("Sorry, no lockers are available.")
        io.wait_enter()
        return

    locker_number = io.get_number_from_list(
        "Available Lockers",
        available_numbers
    )

    contents = io.get_contents()

    success, message = locker_manager.add_rental(
        user["user_name"],
        contents,
        locker_number
    )

    print(f"\n{message}")
    io.wait_enter()


def end_rental(user: dict, locker_manager: LockerManager):
    """
    Allows the current user to end one of their rentals.
    """

    io.clear_screen()

    rentals = locker_manager.get_user_rentals(user["user_name"])

    if not rentals:
        print("You have no lockers rented.")
        io.wait_enter()
        return

    locker_number = io.get_number_from_list(
        "Rented Lockers",
        list(rentals.keys())
    )

    success, message = locker_manager.end_rental(locker_number)

    print(f"\n{message}")
    io.wait_enter()

