# add method adds one element to a set.
# sets do not use indexes and duplicates values are ignored.

colors = {"red", "blue"}
print(colors)

# add new elements to a set
colors.add("green")
colors.add("purple")

print(colors)

# adding element that already exist
colors.add("green")
print(colors)