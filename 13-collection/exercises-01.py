# Shopping cart program

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"Enter the price of {food}:  MZN"))
        foods.append(food)
        prices.append(price)

print("---------YOUR CART ----------")

for food in foods:
    print(food)