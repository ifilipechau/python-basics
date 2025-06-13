# String Methods Example

# name = input("Enter your full name: ")
phone_number = input("Enter your phone number: ")

# result = len(name) # len counts also the spaces between words
# result = name.strip() # Removes leading and trailing whitespace
# result = name.find(" ") # Finds the first occurrence of a space character
# name = name.capitalize() # Capitalizes the first letter of the string
# name = name.upper() # Converts the string to uppercase
# name = name.lower() # Converts the string to lowercase
# result = name.isdigit() # Checks if the string contains only digits
# result = name.isalpha() # Checks if the string contains only alphabetic characters
# result = phone_number.count("-") # Counts the number of hyphens in the phone number
phone_number = phone_number.replace("-", " ") # Removes hyphens from the phone number
print(phone_number)