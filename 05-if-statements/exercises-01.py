# Python calculator


# create a simple calculator that can add, subtract, multiply, and divide two numbers

operator = (input("Enter an operator: ( + - * / ) "))
num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))

if operator == "+":
    result = num1 + num2
    print(result)
elif operator == "-":
    result = num1 - num2
    print(result)
elif operator == "*":
    result = num1 * num2
    print(result)
elif operator == "/":
    result = num1 / num2
    print(round(result, 2))
else:
    print(f"{operator} is not a valid operator")



