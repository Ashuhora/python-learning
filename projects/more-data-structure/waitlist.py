import terminal_utils as term

def add_party(waitlist:list)->None:
    """
    Adds a party to the waitlist

    Args:
        waitlist(list): The waitlist data
    """
    name = term.get_party_name(waitlist)
    size = term.get_party_size()

    party = {
        "name": name,
        "size": size
    }

    waitlist.append(party)
    print(f"{name} has been added to the waitlist.")

def call_next_party(waitlist:list)->None:
    """
    Calls the next party on the waitlist.

    Args:
        waitlist(list): The waitlist data
    """
    if len(waitlist) == 0:
        print("The list is empty!")
        return
    
    party = waitlist.pop(0)

    print(f"Calling {party["name"]}, party of {party["size"]}.")

def remove_party(waitlist:list)->None:
    """
    Remove a party from the waitlist by index

    Args:
        waitlist(list): The waitlist data
    """
    if len(waitlist) == 0:
        print("The waitlist is empty.")
    else:
        # Print the list
        display_waitlist(waitlist)

        try:
            position = int(input("Enter position number to remove: "))

            if position < 1 or position > len(waitlist):
                print("There is no party at that position.")
            else:
                party = waitlist.pop(position - 1)
                print(f"{party["name"]} has been removed from the waitlist.")
        except:
            print("That is not a valid position.")
        
def display_waitlist(waitlist:list)->None:
    """
    Displays a list of parties on the wait list.

    Args:
        waitlist(list): The waitlist data.
    """
    if len(waitlist) == 0:
        print("The waitlist is empty!")
        return
    
    print("Wait List")
    print("==============================")

    for i, party in enumerate(waitlist):
        print(f"{i+1}. {party["name"]} ({party["size"]})")