# This program let's the user create a task list

tasks = []

keep_going = True

while keep_going:
    task = input("Enter a task or 'Q' to quit: ")

    if task == "Q":
        keep_going = False
        continue

    tasks.append(task)

print(f"You have {len(tasks)} tasks")
print(tasks)