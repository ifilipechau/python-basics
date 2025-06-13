# Exercise 2 Shopping Cart Program

item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))
total = price * quantity

print(f"The item you want to buy costs {price}MZN, and total amount you have to pay is {total}MZN.")
print("Thanks for buying with us!")