# This is Simple Calculator

print("Welcome to the Simple Calculator!")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operation = input("Choose an operation (+, -, *, /): ")

if operation == "+":
    print("result:", num1 + num2)

elif operation == "-":
    print("result:", num1 - num2)

elif operation == "*":
    print("result:", num1 * num2)

elif operation == "/":
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        print("result:", num1 / num2)
     
else:
    print("Invalid operation.")