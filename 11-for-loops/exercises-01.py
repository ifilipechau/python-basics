# Count down timer

import time

my_time = int(input("Enter the time in seconds: "))
'''
for x in range(0, my_time): # range starts at 0 and goes to my_time - 1
    print(x)
    time.sleep(5) # Works in seconds, so 5 means 5 seconds 

print("TIME'S UP")
'''
# This is the countdown timer
for x in range(my_time, 0, -1): # range starts at my_time and goes to 1
    seconds = x % 60 # Get the seconds part
    minutes = int(x / 60) % 60 # Get the minutes part
    hours = int(x / 3600) # Get the hours part
    print(f"{hours:02}:{minutes:02}:{seconds:02}") # Print in HH:MM:SS format
    time.sleep(1) # Works in seconds, so 1 means 1 second

print("TIME'S UP")
