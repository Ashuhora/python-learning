# Checking for Elements
# The 'in' keyword checks whether an element exists in a set.
# It returns True if the element is found and False if it is not.

colors = {"red", "green", "blue"}

search = input("Enter a color: ").lower()

if search in colors:
    print(f"The colors {search} was found in the set.")

else:
    print(f"The color {search} was not found in the set.")