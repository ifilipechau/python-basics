# Typecasting is the process of converting one data type to another.
# In Python, typecasting can be done using built-in functions like int(), float(), str(), etc.

# There are two types of typecasting: Explicit and Implicit.
# Explicit typecasting is when you manually convert a data type to another using built-in functions.
# Implicit typecasting is when Python automatically converts one data type to another.

# Example of Explicit Typecasting
name = "Chau"
age = 21
gpa = 4.9
student = True

age = float(age) # Explicitly converting age to float
gpa = int(gpa) # Explicitly converting gpa to int

#print(type(name))
#print(type(age))
#print(type(gpa))
#print(type(student))

# Example of Implicit Typecasting

num1 = 10
num2 = 20.5

result = num1 + num2 # Implicitly converting num1 to float
print(result)
