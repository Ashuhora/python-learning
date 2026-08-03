import terminal_io as io

print("Terminal Input Utility Demo")
print("===========================")

# Demonstrate get_positive_number
print("\nGet Positive Number Demo:")
num = io.get_positive_number("Enter a positive number: ")
print(f"You entered {num}")

# Demonstrate get_yes_no_answer
print("\nYes/No Question Demo:")
likes_python = io.get_yes_no_answer("Do you enjoy learning Python? (yes/no): ")
if likes_python:
    print("Great! Python is an excellent language to learn.")
else:
    print("That's okay! Everyone has different preferences.")

# Demonstrate get_value_in_range
print("\nValue Range Demo:")
age = io.get_value_in_range("Enter your age (1-120): ", 1, 120)
print(f"You entered: {age}")

# Demonstrate get_list_of_values
print("\nList Collection Demo:")
shopping_list = io.get_list_of_values("Please enter your shopping list items:")
print(f"Your shopping list has {len(shopping_list)} items:")
for i, item in enumerate(shopping_list, 1):
    print(f"  {i}. {item}")

# Demonstrate get_choice_from_menu
print("\nMenu Options Demo:")
menu_options = [
    "View all records",
    "Add new record",
    "Edit record",
    "Delete record",
    "Exit"
]

choice = io.get_choice_from_menu(
    "Record System",
    menu_options,
    "Enter your choice: "
)

print(f"You selected: {menu_options[choice]}")

print("\nDemo complete. Thanks for trying these utility functions!")