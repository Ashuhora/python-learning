def get_positive_number(prompt: str) -> int:
    """
    Displays the prompt and returns a positive number.
    """
    while True:
        try:
            val = int(input(prompt))

            if val > 0:
                return val
            else:
                print("That value is not positive!")
        except:
            print("Input must be a positive number.")


def get_choice_from_menu(title, options, prompt="Choose an option: "):
    """
    Displays a numbered menu of options and returns the user's choice.

    Args:
        title (str): The title for the menu
        options (list): List of string menu options to display
        prompt (str): The prompt to display when asking for input

    Returns:
        int: The index of the selected option (0-based)
    """
    # Display the menu
    print(title)
    for i, option in enumerate(options, 1):  # Start numbering from 1
        print(f"{i}. {option}")

    # Get and validate input
    while True:
        try:
            choice = int(input(prompt))

            # Check if the choice is within valid range
            if 1 <= choice <= len(options):
                return choice - 1  # Convert to 0-based index
            else:
                print(f"Please enter a number between 1 and {len(options)}.")
        except ValueError:
            print("Please enter a valid number.")


def get_value_in_range(prompt, min_val, max_val):
    """
    Gets a numeric value within a specified range.

    Args:
        prompt (str): The prompt to display
        min_val (int): Minimum allowed value (inclusive)
        max_val (int): Maximum allowed value (inclusive)

    Returns:
        int: The validated input value
    """
    while True:
        try:
            val = int(input(prompt))

            # Check against min and max if they're provided
            if val < min_val or val > max_val:
                print(f"Please enter a value between {min_val} and {max_val}.")
            else:
                return val
        except:
            print("Please enter a valid number.")


def get_list_of_values(prompt, stop_value="Q"):
    """
    Collects a list of values until the user enters the stop value.

    Args:
        prompt (str): The prompt to display for each value
        stop_value (str): The value that signals the end of input

    Returns:
        list: The collected values
    """
    values = []

    # Explain to the user how to stop input
    print(prompt)
    print(f"Enter values one at a time. Type '{stop_value}' when finished.")

    while True:
        # Get next value, numbering for the user based on list size
        value = input(f"{len(values) + 1}: ")

        if len(value.strip()) == 0:
            print("You must enter a value.")
            continue

        # Check for stop value
        if value.upper() == stop_value.upper():
            break

        values.append(value)

    return values


def get_yes_no_answer(prompt):
    """
    Gets a yes/no answer from the user.

    Args:
        prompt (str): The question to ask

    Returns:
        bool: True for yes, False for no
    """
    # A neat trick is to use a list containing all viable entries
    valid_yes = ["yes", "y"]
    valid_no = ["no", "n"]

    while True:
        answer = input(prompt).lower()

        # Check if the user answer is in the list of valid values
        if answer in valid_yes:
            return True
        elif answer in valid_no:
            return False
        else:
            print("Please enter yes or no.")