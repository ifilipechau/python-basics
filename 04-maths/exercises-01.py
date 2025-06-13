# Exercise 01 - Calculate the hypotenuse of a triangle

import math

a = float(input("Enter the side A of the triangle: "))
b = float(input("Enter the side B of the triangle: "))

# Calculate the hypotenuse using the Pythagorean theorem
c = math.sqrt(a ** 2 + b ** 2)

# This is the other formula to make it 
# c = math.sqrt(pow(a, 2) + pow(b, 2))


# Print the result
print(f"The hypotenuse of the triangle with sides {a} and {b} is: {c:.2f}")
