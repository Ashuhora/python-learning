# This method delets element form a set
# if the element does not exist it throw a key error.

colors = {"red", " green", "blue"}
print(colors)

# remove element
colors.remove("red")
print(colors)

# This will causes KeyError
 colors.remove(yellow)