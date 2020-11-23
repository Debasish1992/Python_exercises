computer = {
    "name": "Hp Elite Series",
    "model": "es24",
    "brand": "HP",
    "year": 2020
}
print(computer)

print(len(computer))

print(type(computer))

get_key_list = computer.keys()
print(get_key_list)
get_values_list = computer.values()
print(get_values_list)
get_item_list = computer.items()
print(get_item_list)

computer.update({"year": 1200})
print(computer)

if "branded" in computer:
    print("Exist")
else:
    print("Does not exist")

for items in get_key_list:
    print(items)

for items in computer:
    print(items.capitalize())

bike = {
    "name": "Pulsar 220",
    "color": "blue",
    "power": "550 CC",
    "year": 2020
}

bike_2 = bike.copy()

print(bike_2)

bike_3 = dict(bike)
print(bike_3)

