given_string = input("Enter copying string: ")
copy_times = int(input("Enter the number of times to copy the string: "))


def copy_string(str, n):
    defined_str = "This is a new day"
    for items in range(n):
        defined_str = defined_str + str
    return defined_str


print(copy_string(given_string, copy_times))
