"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Weijie Zeng
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer.
# Validate that they have entered an integer.
user_input = input("Enter your monthly savings amount: ")
try:
    monthly = int(user_input.strip())
    annual_saving = monthly * 12
    total = annual_saving * 1.008
    print(f"You will save £{annual_saving} every year.")
# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
# print this out in the format £X.XX (to two decimal places).
    print(f"With interest, you will save £{total:.2f} per year.")
except ValueError:
    print("Invalid amount")
