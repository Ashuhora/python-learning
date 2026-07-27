# Start the wait list empty 
waitlist = []

while True:
    # Display menu
    print("\n===== Restaurant Waitlist Manager =====")
    print("1. View the Waitlist")
    print("2. Add a Party")
    print("3. Call Next Party")
    print("4. Remove a Party")
    print("5. Quit")
    
    choice = input("\nEnter your choice: ")
    
    if choice == "1":
        # View Waitlist
        # Check if the wait list is empty
        if not waitlist:
            print("The waitlist is empty.")
        else:
            print("Current Waitlist:")
            for i, party in enumerate(waitlist):
                print(f"{i + 1}. {party}")
    
    elif choice == "2":
        # Add a Party
        party_name = input("Enter party name: ")
        waitlist.append(party_name)
        print(f"{party_name} has been added to the waitlist.")
    
    elif choice == "3":
        # Call Next Party
        if not waitlist:
            print("The waitlist is empty.")
        else:
            next_party = waitlist.pop(0)
            print(f"{next_party} has been called and removed from the waitlist.")
    
    elif choice == "4":
        # Remove a Party
        if not waitlist:
            print("The waitlist is empty.")
        else:
            # First show the current waitlist
            print("Current Waitlist:")
            for i, party in enumerate(waitlist):
                print(f"{i + 1}. {party}")
            
            # Ask for position to remove
            position = int(input("Enter position number to remove: "))
            if position < 1 or position > len(waitlist):
                print("There is no party at that position.")
            else:
                removed_party = waitlist.pop(position - 1)
                print(f"{removed_party} has been removed from the waitlist.")
    
    elif choice == "5":
        # Quit
        print("Thank you for using the Restaurant Waitlist Manager. Goodbye!")
        break
    
    else:
        # Invalid choice
        print("Invalid choice. Please try again.")