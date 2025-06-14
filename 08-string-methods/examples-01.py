# indexing = accessing elements of a sequence using [] (indexing operator)
#           [start : end : step]

credit_number = "1234-5678-9012-3456"

# print(credit_number[0]) # The first character in the string
# print(credit_number[:4]) # The first 4 characters in the string
# print(credit_number[5:9]) # The 4 digits after the first hyphen
# print(credit_number[5:]) # The string after the first hyphen
# print(credit_number[::2]) # Every second character in the string
# print(credit_number[-1]) # The last number in the string
# print(credit_number[::2]) # will print every second character within the string

# last_digits = credit_number[-4:] # Get the last 4 digits of the credit card number
# print(f"XXXX-XXXX-XXXX-{last_digits}") # Print the last 4 digits of the credit card number

credit_number = credit_number[::-1] # Reverse the credit card number
print(credit_number) # Print the reversed credit card number