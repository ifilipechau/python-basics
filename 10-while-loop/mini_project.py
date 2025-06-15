# Python compund interest calculator
# This program calculates the compound interest for a given principal amount, rate of interest, and time period.

principal = 0
rate = 0
time = 0

while principal <= 0:
    principal = float(input("Enter the principle amount: "))
    if principal <= 0:
        print("Principal can't be less than or equal to zero")

print(principal)