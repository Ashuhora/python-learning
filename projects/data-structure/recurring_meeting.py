from datetime import datetime, timezone, timedelta

def get_current_datetime():
    """
    Return:
    - Current local date and time
    - Current UTC date and time
    - Time difference (offset) between local time and UTC
    """
    # Get the current local date and time
    local_dt = datetime.now()

    # Get the current UTC date and time
    utc_dt = datetime.now(timezone.utc)

    # Calculate the UTC offset in hours
    # Example: Local = 1 PM, UTC = 6 PM → offset = -5
    offset = int((local_dt.hour - utc_dt.hour))

    return (local_dt, utc_dt, offset)


def get_value_in_range(prompt, min_value, max_value):
    """
    Ask the user for a number until they enter
    a value within the allowed range.
    """
    while True:
        try:
            # Convert the user's input into an integer
            value = int(input(prompt))

            # Check if the value is within the allowed range
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Please enter a value between {min_value} and {max_value}.")

        # Handle non-numeric input
        except ValueError:
            print("Please enter a valid number.")


def get_start_date():
    """Prompt the user to enter a valid meeting date."""

    # Get the current year
    current_year = datetime.now().year

    while True:
        try:
            # Ask for the year
            year = get_value_in_range(
                "Enter year (YYYY): ",
                current_year,
                current_year + 1
            )

            # Ask for the month
            month = get_value_in_range(
                "Enter month (1-12): ",
                1,
                12
            )

            # Ask for the day
            day = get_value_in_range(
                "Enter day (1-31): ",
                1,
                31
            )

            # Create a datetime object.
            # If the date is invalid (like Feb 30),
            # Python raises a ValueError.
            date_obj = datetime(year, month, day)

            return date_obj

        except ValueError:
            print("Invalid date. Please try again.")


def get_occurrences():
    """Ask how many meetings to schedule."""
    return get_value_in_range(
        "Number of occurrences: ",
        1,
        52
    )


def get_frequency():
    """Ask whether meetings repeat daily or weekly."""

    # Valid options
    valid_options = ['d', 'w']

    while True:
        # Read the user's choice
        frequency = input(
            "Frequency (d=Daily, w=Weekly): "
        ).lower()

        # Return the value if it is valid
        if frequency in valid_options:
            return frequency

        print("Invalid option. Please enter d or w.")


def create_meeting_schedule(start_date, utc_offset, occurrences, frequency):
    """
    Create a list of recurring meetings.

    Parameters:
    start_date  - First meeting (local time)
    utc_offset  - Difference between local and UTC
    occurrences - Number of meetings
    frequency   - d = daily, w = weekly

    Returns:
    A list of tuples:
    (local_time, utc_time)
    """

    # Store all meetings here
    schedule = []

    # Start with the first meeting
    current_date = start_date

    # Repeat for the requested number of meetings
    for i in range(occurrences):

        # Convert local time into UTC
        utc_time = current_date + timedelta(hours=-utc_offset)

        # Save both local and UTC times
        schedule.append((current_date, utc_time))

        # Move to the next meeting
        if frequency.lower() == 'd':
            # Next day
            current_date = current_date + timedelta(days=1)

        elif frequency.lower() == 'w':
            # Next week
            current_date = current_date + timedelta(weeks=1)

    return schedule


def format_meeting_schedule(meeting_schedule):
    """Create a nicely formatted schedule as a string."""

    # Start the output text
    result = "Your meeting schedule:\n"

    # Loop through every meeting
    for i, (local_time, utc_time) in enumerate(meeting_schedule, 1):

        # Add the meeting number and times
        result += (
            f"Meeting {i}: "
            f"{local_time.strftime('%Y-%m-%d %H:%M:%S')} (Local) | "
            f"{utc_time.strftime('%Y-%m-%d %H:%M:%S')} (UTC)\n"
        )

    return result