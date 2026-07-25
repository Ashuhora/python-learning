
# This shows how to use the index method to find values in a list.
# In this example, first and second time the value appears.
nums = [1, 2, 3, 2, 5]

found1 = nums.index(2)
found2 = nums.index(2, found1 + 1)

print(f"There is a 2 at index {found1}")
print(f"There is another 2 at index {found2}")