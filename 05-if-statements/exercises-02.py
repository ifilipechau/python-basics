# Python weight conversion program
# This program converts a weight from pounds to kilograms or vice versa based on user input.

# Get user input for weight and unit
weight = float(input("Enter the weight: "))
unit = input("Is this weight in pounds (lbs) or kilograms (kg)? Enter 'lbs' or 'kg': ").strip().lower()

# check the unit and perform the conversion
if unit == "kg":
    weight = weight * 2.205
    unit = "lbs"
    print(f"Your weight is: {round(weight, 2)} {unit}")
elif unit == 'lbs':
    weight = weight / 2.205
    unit = "kg"
    print(f"Your weight is: {round(weight, 2)} {unit}")
else:
    print(f"{unit} was not valid")
