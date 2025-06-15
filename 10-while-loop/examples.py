# While loop = execute a block of code as long as a condition is True

# Example 1: Basic while loop
name = input("Enter your name: ")

'''
if name == "":
    print("You did not enter your name")
else:
    print(f"Hello {name}")

'''

while name == "":
    print("You did not enter your name")
    name = input("Enter your name: ")

print(f"Your name is {name}")