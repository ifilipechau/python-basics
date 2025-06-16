# nested loop 2

rows = int(input("Enter number of rows: "))
column = int(input("Enter number of columns: "))
symbol = input("Enter symbol to use: ")

for x in range(rows):
    for y in range(column):
        print(symbol, end="") # end parameter prevents new line after each print
    print() # New line after inner loop completes 