# conditional expression = A one-line shortcut for the if-else statement (ternary operator).
#                          Print or assign one of two values based on a condition.
#                          X if condition else Y

num = 7

# print("Positive" if num > 0 else "Negative or Zero")
result = "EVEN" if num % 2 == 0 else "ODD"
print(result)