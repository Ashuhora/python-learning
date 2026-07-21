# Tip Calculator
# This program calculates the tip amount and total bill.

bill_amount = float(input("Enter the total bill amount: $"))


tip_percentage = int(input("Enter the tip percentage: "))


tip = bill_amount * tip_percentage / 100


total_bill = bill_amount + tip


print(f"Tip amount: ${tip:.2f}")
print(f"Total bill: ${total_bill:.2f}")