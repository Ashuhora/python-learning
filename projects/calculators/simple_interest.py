# Simple Interest Calculator

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in%): "))
time = float(input("Enter the time in years: "))

interest = (principal * rate * time) / 100
print(f"The simple interest on ${principal:.2f} at {rate:.1f}% for {time:.1f} years is ${interest:.2f}.")