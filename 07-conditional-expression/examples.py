# conditional expression = A one-line shortcut for the if-else statement (ternary operator).
#                          Print or assign one of two values based on a condition.
#                          X if condition else Y

num = 7
a = 9
b = 10
age = 16

# print("Positive" if num > 0 else "Negative or Zero")
# result = "EVEN" if num % 2 == 0 else "ODD"
# print(result)

# max_num = a if a > b else b
# print(max_num)

# min_num = a if a < b else b
# print(min_num)

status = "You are an adult" if age >= 18 else "You are just a kid"
print(status)