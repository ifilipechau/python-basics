# format specifiers = {:flags} format a value based on what flags are inserted
# flags = 0, +, -, , (space), #, 0

# . (number)f = round to number of decimal places
# : (number) = allocate that many spaces for the value
# :03 = allocate and zero pad that many spaces for the value
# :< = left align
# :> = right align
# :^ = center align

def format_specifiers():
    # Example 1: Basic formatting
    value = 123.456789
    print(f"Value: {value:.2f}") # Round to 2 decimal places
    print(f"Value: {value:10.2f}") # Allocate 10 spaces, round to 2 decimal places
    print(f"Value: {value:<10.2f}") # Left align in 10 spaces, round to 2 decimal places
    print(f"Value: {value:>10.2f}") # Right align in 10 spaces, round to 2 decimal places
    print(f"Value: {value:^10.2f}") # Center align in 10 spaces, round to 2 decimal places
    print(f"Value: {value:03.2f}") # Allocate 3 spaces, zero pad, round to 2 decimal places
    print(f"Value: {value:0<10.2f}") # Left align, zero pad in 10 spaces, round to 2 decimal places
    print(f"Value: {value:0>10.2f}") # Right align, zero pad in 10 spaces, round to 2 decimal places

    # Examples 2
    price1 = 30000.14159
    price2 = -9830.65
    price3 = 1200.34

    print(f"Price 1: {price1:,.2f} MZN") # Comma as thousands separator, 2 decimal places
    print(f"Price 2: {price2:,.2f} MZN") # Comma as thousands separator, 2 decimal places
    print(f"Price 3: {price3:,.2f} MZN") # Comma as thousands separator, 2 decimal places

format_specifiers()
