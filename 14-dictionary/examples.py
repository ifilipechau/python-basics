# dictionary = a colletion of {key: value} pairs
#               ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}


# print(dir(capitals)) # to see all the methods and attributes of the dictionary
# print(help(capitals)) # To see all the descriptions of the attributes and methods

# print(capitals.get("USA"))

# Check if a key is within a dictionary

# if capitals.get("Japan"):
#    print("That capital exist")
#else:
#    print("That capital doesn't exist")

    # To insert a new value key-pair or update the existing ones
# capitals.update({"Mozambique": "Maputo"})
# capitals.update({"USA": "New York"})
# print(capitals)

    # To remove a key-pair value
# capitals.pop("China")
# print(capitals)

# capitals.popitem()
# capitals.clear()

# keys = capitals.keys()
# for key in capitals.keys():
#   print(key)

# values = capitals.values()

# for value in capitals.values():
#    print(value, end = " ")

items = capitals.items()
for key, value in capitals.items():
    print(f"{key}:{value}")
