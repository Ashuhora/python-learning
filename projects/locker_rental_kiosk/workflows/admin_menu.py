"""
Admin function for locker rental kiosk.
"""
# import terminal input and display functions
from workflows import terminal_io as io
from managers.locker_manager import LockerManager

def start_workflows(user: dict, locker_manager: LockerManager):
    """
    This runs the menu for an admin.
    """
    # Keep showing the admin menu until the admin logs out
    while True:
        choice = admin_menu()

        if choice == "1":
            view_rentals(locker_manager)

        elif choice == "2":
            end_rentals(locker_manager)

        elif choice == "3":
            clear_log(locker_manager)

        elif choice == "4":
            print(f"\nLogging out. Have a great day,"
                  f"{user['user_name']}"
            )
            return

def admin_menu() -> str:
    """
    Display the Admin menu.
    """
    io.clear_screen()

    print("Locker Rental Kiosk Admin Menu")
    print("-" * 60)
    print("1. view REntals")
    print("2. End Rental")
    print("3. Clear Log")
    print("4. Log Out")
    print()

    return io.get_menu_choice("Enter choice (1-4): ", ["1", "2", "3", "4"])

def view_rentals(Locker_manager: LockerManager):
    """
    This displays all rented lockers.
    """
    io.clear_screen()

    rentals = LockerManager.get_all_rentals()

    if not rentals:
        print("There are no lockers rented.")
    else:
        io.display_lockers(rentals)

    # Pause until the admin presses Enter
    io.wait_enter()

def end_rental(locker_manager: LockerManager):
    """
    Allow the adminstrator to end any rental.
    """
    io.clear_screen()

    rentals = locker_manager.get_all_rentals()

    if not rentals:
        print("There are no lockers rented.")
        io.wait_enter()
        return

    io.display_lockers(rentals)

    locker_number = io.get_number_from_list("Rented Lockers", rentals.keys())

    success, message = locker_manager.end_rental(locker_number)

    print(f"\n{message}")
    io.wait_enter()

def clear_log(Locker_manager: LockerManager):
    """
    clears all messages from the log file.
    """
    io.clear_screen()

    if Locker_manager.log_manager.clear_log():
        print("Log has been cleared.")
    else:
        print("Log could not be cleared")

    io.wait_enter()


 
