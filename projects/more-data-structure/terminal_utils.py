import os

def clear_screen():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Linux/Mac
    else:
        os.system('clear')

def get_party_name(waitlist:list)->str:
    """
    Gets a party name to add to the list.
    The name must not already exist on the waitlist.

    Args:
        waitlist(list): The waitlist data.
    Returns:
        str: A unique name to be added to the waitlist.
    """
    while True:
        name = input("Enter the name of the party: ").strip().title()

        for party in waitlist:
            if name == party["name"]:
                print("That name is already on the waitlist.")
                continue

        if len(name) == 0:
            print("The party name cannot be blank.")
        else:
            return name

def get_party_size()->int:
    """
    Prompts the user for the number of party members.

    Returns:
        int: The size of the party.
    """
    while True:
        try:
            count = int(input("Enter the # of party members: "))

            if count < 1:
                print("There must be at least one party member!")
            else:
                return count
        except:
            print("That is not a valid number.")

def display_menu()->str:
    """
    Clears the screen then displays the main menu

    Returns:
        str: A valid menu choice
    """
    clear_screen()

    while True:
        valid_choices = ["1", "2", "3", "4", "5"]

        print("\n===== Restaurant Waitlist Manager =====")
        print("1. View the Waitlist")
        print("2. Add a Party")
        print("3. Call Next Party")
        print("4. Remove a Party")
        print("5. Quit")
        
        choice = input("\nEnter your choice (1-5): ")

        if choice in valid_choices:
            return choice
        
        print("That was not a valid choice!")