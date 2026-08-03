import recurring_meeting as rm
from datetime import datetime

# Display the program title
print("Recurring Meeting Scheduler")
print("==========================\n")

# Get the current local time, UTC time, and UTC offset
local_dt, utc_dt, offset = rm.get_current_datetime()

# Display the current date and time information
print(f"Current Local Time: {local_dt.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Current UTC Time: {utc_dt.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Offset: {offset}\n")

# Ask the user to enter meeting information
print("Please enter meeting details:")

# Get the meeting start date
start_date = rm.get_start_date()

# Get the meeting hour (0-23)
hour = rm.get_value_in_range("Enter hour (0-23): ", 0, 23)

# Get the meeting minute (0-59)
minute = rm.get_value_in_range("Enter minute (0-59): ", 0, 59)

# Combine the date with the hour and minute entered by the user
# Seconds are set to 0
start_datetime = start_date.replace(hour=hour, minute=minute, second=0)

# Ask how many meetings to create
occurrences = rm.get_occurrences()

# Ask whether meetings repeat daily or weekly
frequency = rm.get_frequency()

# Create the recurring meeting schedule
schedule = rm.create_meeting_schedule(
    start_datetime,
    offset,
    occurrences,
    frequency
)

# Display the formatted schedule
print("\n" + rm.format_meeting_schedule(schedule))