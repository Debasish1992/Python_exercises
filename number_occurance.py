list_1 = [1, 4, 6, 2, 4, 4, 19]
list_2 = [1, 3, 4, 7, 20, 4, 19]


def find_occurance(list):
    counter = 0
    for item in list:
        if item == 4:
            counter += 1
    return counter


print(find_occurance(list_1))
print(find_occurance(list_2))
