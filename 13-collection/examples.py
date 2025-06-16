# collection = single "variable" used to store multiple values
#   list = [] ordered and changeable. Duplicates OK
#   Set  = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchangeale. Duplicates OK. FASTER

fruits = ["apple", "orange", "banana", "coconut"]
# print(dir(fruits)) # we use dir() to see the methods available for the list
# print(help(fruits)) # we use help() to see the documentation for the list methods
# print(len(fruits)) # returns the number of items in the list
# print("apple" in fruits)


# print(fruits[0:3]) # we use slicing to get a range of values
# print(fruits[0:]) # we can also use slicing to get all values
# print(fruits[::2]) # we can use slicing to get every second value
# print(fruits[::-1]) # we can use slicing to reverse the list

# for fruit in fruits: # we can use a for loop to iterate over the list
#    print(fruit)