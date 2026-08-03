"""
Main programm for the locker rental kiosk.
"""
# import classes

from managers.log_manager import LogManager
from managers.locker_manager import LockerManager
from managers.user_manager import UserManager
from workflows import terminal_io as io
from workflows import admin_menu
from workflows import user_menu

def login_workflow(user_manager: UserManager, locker_manager: LockerManager):
    """
    Allows an existing user to login.
    """
    io.clear_screen()

    print("User Login")
    print("_" * 50)

    user_name = io.get_user_name("User Name: ")
    pin = io.get_pin()

    # check the log in info
    user = user_manager.login(user_name, pin)

    if not user:
        print("\nInvalid username or PIN.")
        io.wait_enter()
        return

    print(f"\nWelcome back, {user['user_name']}!")
    io.wait_enter()

    if user["is_admin"]:
        admin_menu.start_workflow(user, locker_manager)
    else:
        user_menu.start_workflow(user, locker_manager)

def register_workflow(user_manager: UserManager, locker_manager: LockerManager):
    """
    Allow a new user to register.
    """
    io.clear_screen()

    print("User Registration")
    print("_" * 50)

    while True:
        user_name = io.get_user_name("Enter the username: ")

        # ask again if the name already exists
        if user_manager.user_exists(user_name):
            print("This username is not available.")
            continue

        pin = io.get_pin()

        success, message, user = user_manager.add_user(user_name, pin)

        print(f"\n{message}")

        if not success:
            io.wait_enter()
            return

        print(f"Welcome, {user_name}!")
        io.wait_enter()

        # This sends the new user directly to the user menu
        user_menu.start_workflow(user, locker_manager)
        return

def main():
    """
    starts and runs the locker rental kiosk.
    """
    # create the manager object

    log_manager = LogManager()
    user_manager = UserManager(log_manager)
    locker_manager =LockerManager(log_manager)

    # this keeps the kiosk running
    while True:
        choice = io.main_menu()

        if choice == "1":
            login_workflow(user_manager, locker_manager)
        elif choice == "2":
            register_workflow(user_manager, locker_manager)
        elif choice == "3":
            print("\nThank you for using the kiosk. "
            "Have a great day!")
            break

