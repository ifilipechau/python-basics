# Exercise 02 - Calculate the area of shapes

# Area of a rectangle
lenght = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = lenght * width
print(f"The area of the rectangle is: {area} square units.")

# Area of a circle
import math
radius = float(input("Enter the radius of the circle: "))
area_circle = math.pi * (radius ** 2)
print(f"The area of the circle is: {area_circle:.2f} square units.")

# Area of a tringle
base = float(input("Enter the lenght of the base: "))
height = float(input("Enter the height of the triangle: "))
area = (base * height)/2
print(f"The area of the triangle is: {area}")
