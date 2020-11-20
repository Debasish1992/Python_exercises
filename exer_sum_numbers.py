first_number = int(input("Enter the first number:- "))
second_number = int(input("Enter the second number:- "))
third_number = int(input("Enter the third number:- "))


def sum_thrice(x, y, z):
    sum = x + y + z
    if x == y == z:
        sum *= 3
    return sum


print(sum_thrice(first_number, second_number, third_number))
