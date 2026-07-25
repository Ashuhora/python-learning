# This shows how to use the in keyword to check if a value exists in a list.
# if that value is in the list.

nums = [1, 2, 3, 2, 5]

target = int(input("Enter a value to search for: "))

if target in nums:
    print(f"{target} was found in the list.")
else:
    print(f"{target} was not found in the list.")