# Python basics practice.
# This file contains examples from class.
# and my own practice examples.
# =================================================
print("Hello, World!")
print("My name is Nahum.")
print("I am learning Python.")
# ==================================================
# Integer is a whole number
number_of_students = 10

#A float is a number with a decimal point.
class_time = 7.5

print(number_of_students)
print(class_time)
# ======================================================
# Math operations.
x = 6
y = 2

print(x + y)   # Addition
print(x - y)   # Subtraction
print(x * y)   # Multiplication
print(x / y)   # Division
print(x // y)  # Integer division
print(x ** y)  # Exponent

# =========================================================

# Order of operations
# Multiplication happens before addition. (PEMDAS)
print(1 + 2 * 3)

# Parentheses make addition happen first.
print((1 + 2) * 3)

# Underscores help to read large numbers easier. 
million = 2_000_000

print(million)
# =========================================================
# Boolean values can be True or False

x = 9
y = 5

print(f"Is {x} greater than {y}? {x > y}")
print(f"Is {x} less than {y}? {x < y}")

# Another comparison example

current_score = 91
passing_score = 80

print(f"Did the student pass? {current_score >= passing_score}")

# Boolean logic

has_username = True
has_password = True

print(f"Can the user log in? {has_username and has_password}")

# With or, only one condition needs to be True.

has_cash = False
has_card = True

print(f"Can the customer pay? {has_cash or has_card}")

# A transaction is allowed when:
# 1. The account remains positive or overdraft is allowed.
# 2. The account status is open.

balance = 500.25
transaction = -250
status = "Open"
allow_overdraft = True

allow_transaction = (
    ((balance + transaction > 0) or allow_overdraft)
    and (status == "Open")
)

print(f"Allow transaction? {allow_transaction}")

# =========================================================

# Formatting text into a table

fruit1 = "Apple"
price1 = 0.50

fruit2 = "Banana"
price2 = 0.75

fruit3 = "Cherry"
price3 = 1.00

# Print the table header.
# <10 means left-align inside a space of 10 characters.
# >10 means right-align inside a space of 10 characters.

print(f"{'Fruit':<10} | {'Price':>10}")
print(f"{'-' * 10} | {'-' * 10}")

# .2f displays two numbers after the decimal point.

print(f"{fruit1:<10} | ${price1:>9.2f}")
print(f"{fruit2:<10} | ${price2:>9.2f}")
print(f"{fruit3:<10} | ${price3:>9.2f}")