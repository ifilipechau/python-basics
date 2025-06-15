# nested loop = A loop within another loop (outer, inner)
#               outer loop:
#                    inner loop:
for x in range(3):
    for y in range(1, 10):
        print(y, end="")
    print() # New line after inner loop completes

# Multiplication table using nested loops
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i * j:2}", end=" ")
    print() # New line after inner loop completes

    