# The discard method removes an element from a set.
# If the element does not exist, no error is raised.

colors = {"red", " green", "blue"}
print(colors)

# discard an existing element

colors.discard("red")
print(colors)

# no issues, the element is ignored if it does not exsist
colors.discard("purple")
print(colors)
