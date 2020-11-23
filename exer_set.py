uniques_set = {"banana", "apple", "kiwis", "tasty_buds"}
for items in uniques_set:
    print(items)
print(len(uniques_set))
uniques_set.add("watermellon")
uniques_set.add("carrot")
print(uniques_set)
print(len(uniques_set))
print(type(uniques_set))
tropical = {"pineapple", "mango", "papaya"}
tropical_list = ["pineapple_list", "mango_list", "papaya_list"]
uniques_set.update(tropical)
uniques_set.update(tropical_list)
print(uniques_set)
if "abc" in uniques_set:
    uniques_set.remove("abc")
else:
    print("The given item does not exist in the list")

uniques_set.discard("abc")

if "banana" in uniques_set:
    print("This is exist in the list")
else:
    print("This does not exist in the list")

direction_set = {"North", "South", "East", "West"}
print(direction_set)
direction_set.pop()
print(direction_set)


cricket_set = {"Australia", "India", "NewZealand", "South Africa", "Sri Lanka"}
football_set = {"Argentina", "Germany", "Spain", "Brazil"}

union_set = cricket_set.union(football_set)
print(union_set)

set_1 = {"a", "b", "c", "d", "e"}
set_2 = {"d", "b", "a", "z", "p"}
set_1.intersection_update(set_2)
print(set_1)
set_1.symmetric_difference(set_2)
print(set_1)
set_1.symmetric_difference_update(set_2)
print(set_1)



