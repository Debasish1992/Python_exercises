
def find_number():
    is_number_exist = False
    list_1 = [1, 5, 8, 3]
    number = int(input("Enter the number: - "))
    for items in list_1:
        if items == number:
            is_number_exist = True
            break

    if is_number_exist:
        print("The number exist")
    else:
        print("The number does not exist")

find_number()