# While loop = execute a block of code as long as a condition is True

# Example 1: Basic while loop
name = input("Enter your name: ")

'''
# Example - Using if

if name == "":
    print("You did not enter your name")
else:
    print(f"Hello {name}")

'''

'''
Example 1 - Using the previous examples but implement it with while loop

while name == "":
    print("You did not enter your name")
    name = input("Enter your name: ")

print(f"Your name is {name}")

'''
# Example 2

age = int(input("Enter your age: "))

while age < 0:
    print("Age can't be negative")
    age = int(input("Enter your age: "))

print(f"You are {age} years old")