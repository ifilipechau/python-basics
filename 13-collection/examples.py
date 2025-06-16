# collection = single "variable" used to store multiple values
#   list = [] ordered and changeable. Duplicates OK
#   Set  = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchangeale. Duplicates OK. FASTER

fruits = ["apple", "orange", "banana", "coconut"]

# print(fruits[0:3]) # we use slicing to get a range of values
# print(fruits[0:]) # we can also use slicing to get all values
# print(fruits[::2]) # we can use slicing to get every second value
# print(fruits[::-1]) # we can use slicing to reverse the list

# for fruit in fruits: # we can use a for loop to iterate over the list
#    print(fruit)