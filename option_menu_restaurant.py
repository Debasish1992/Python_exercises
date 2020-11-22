first_list = ["apple", "banana", "apple", "plum",
              "watermellon", "apple", ("apple", "plum")]
first_set = {"apple"}
for items in first_list:
    first_set.add(items)
print(first_set)
first_set.remove("apple")
print(first_set)