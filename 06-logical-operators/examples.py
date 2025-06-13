# logical operators = evaluate multiple conditions (or, and, not)
#                   or = at least one condition must be True
#                   and = both conditions must be True
#                   not = inverts the condition (not False, not True)

'''
temp = 38
is_raining = False

# OR
if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still sheduled")
'''

temp = 25
is_sunny = True
'''
# AND
if temp >= 28 and is_sunny:
    print("It is HOT outside")
    print("It is SUNNY")
elif temp <= 0 and is_sunny:
    print("It is COULD outside")
    print("It is SUNNY")
elif 28 > temp > 0 and is_sunny:
    print("It is WARM outside")
    print("It is SUNNY")
'''
# NOT
if not is_sunny:
    print("It is NOT sunny outside")
else:
    print("It is sunny outside")