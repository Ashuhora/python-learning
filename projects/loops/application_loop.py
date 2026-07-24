# This program demonstrates an application loop.
# The program keeps running until the user chooses to quit.

keep_running = True

while keep_running:
    print("===== My Application =====")
    print("1. Say Hello")
    print("2. Quit\n")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Hello user!")

    elif choice == "2":
        print("Goodbye!")
        keep_running = False

    else:
        print("That is not a valid choice!")