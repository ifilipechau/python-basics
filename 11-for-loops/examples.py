# for loops = execute a block of code a fixed number of times.
#               you can iterate over a range, string, sequence, etc.

for x in (range(1, 5)): # count from 1 to 4
    print(x)
print("**************************")

for x in reversed(range(1, 4)): # count from 3 to 1
    print(x)

print( "Happy new year!")

print("**************************")
for x in (range(1, 10, 2)): # count from 1 to 9, skipping every second number
    print(x)
