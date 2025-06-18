# Examples of a 2D list in Python

# where the first index is the row and the second index is the column.
# so groceries[2] is the third row (meats) and [2] is the third column (pork).
# so groceries[2][2] is the third item in the third row.

fruits = ["apple", "Orange", "banna", "kiwi"]
vegetables = ["carrot", "broccoli", "spinach", "potato"]
meats = ["chicken", "beef", "pork", "fish"]

groceries = [fruits, vegetables, meats]

print(groceries[2][2]) # Output: pork
print(groceries[0][1]) # Output: Orange
print(groceries[1][2]) # Output: spinach