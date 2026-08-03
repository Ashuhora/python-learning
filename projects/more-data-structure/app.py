import waitlist as wl
import terminal_utils as term

# Start the wait list empty
waitlist = []

while True:
    # Display menu
    choice = term.display_menu()
    
    if choice == "1":
        wl.display_waitlist(waitlist)
    elif choice == "2":
        wl.add_party(waitlist)
    elif choice == "3":
        wl.call_next_party(waitlist)    
    elif choice == "4":
        wl.remove_party(waitlist)
    elif choice == "5":
        # Quit
        print(
            "Thank you for using the Restaurant Waitlist Manager.\n"
            "Goodbye!"
        )
        break

    input("\npress any key to continue...")