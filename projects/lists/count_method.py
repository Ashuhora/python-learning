
# This will asks the user for a value, counts how many times
# it appears in the list, and removes all matching values,.

nums = [1, 2, 3, 2, 5]

target = int(input("Enter a value to remove all: "))

print(f"We found {nums.count(target)} elements with the value {target}.")

while nums.count(target) > 0:
    nums.remove(target)

print(nums)