# For loops example 2

'''
credit_card = "1234-5678-9012-3456"

for x in credit_card:
    print(x)
'''

for x in range(1, 21): # count from 1 to 20 
    if x == 13:
        continue # skip the number 13 and continue to the next iteration, 
    else:        # we could also use 'break' instead of 'continue' to stop the loop (in 12th iteration)
        print(x)