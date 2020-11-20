# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
from datetime import date
import math


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Function responsible for getting the python version
def getPythonVersion():
    version = sys.version_info
    print(version)


def getdateandtime():
    today = date.today()
    d2 = today.strftime("%B %d, %Y")
    print(d2)


def calculateAreaOfCircle():
    radius = int(input("Enter Radius: "))
    if radius == 0:
        print("Please enter a valid radius")
    elif radius < 0:
        print("Please enter a valid radius")
    else:
        area = 3.14 * radius
        area = math.floor(area)
        print("The area of the circle is {result}".format(result=area))


def reverseName():
    firstName = input("Enter first name: ")
    lastName = input("Enter second name: ")

    fullname = firstName + " " + lastName
    fullname = fullname[::-1]
    print(fullname)


def createList():
    index = 0
    list = []
    while index < 5:
        index += 1
        number = int(input("Enter number "))
        list.append(number)
    print(list)


def get_extension():
    file_name = input("enter file name:-")
    file_name_list = file_name.split(".")
    extension = file_name_list[1]
    print(extension)


def fetch_color():
    color_list = ["Cyan", "Green", "White", "Blue"]
    first_color = color_list[0]
    last_color = color_list[-1]
    print("First Color " + first_color)
    print("Last Color " + last_color)


def get_examination_schedule():
    exam_st_date = (11, 12, 2014)
    date = exam_st_date[0]
    month = exam_st_date[1]
    year = exam_st_date[2]
    print("The examination will start from : %i / %i / %i" % exam_st_date)
    print("The exam will start from: {date} / {month} / {year}".format(date=date, month=month, year=year))


def list_methods():
    dummy_list = ["Hello", "World", "My Home", 10, 56, 278]
    print(dummy_list)
    dummy_list.append("Test my plan")
    print(dummy_list)
    dummy_list.extend([10, 46, "tasty"])
    print(dummy_list)


def add_items_to_list():
    list = []
    for items in range(10):
        list.append(items)
    print(list)
    print(list[::-1])
    list.pop()
    list.remove(4)
    print(list)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # calculateAreaOfCircle()
    # reverseName()
    # createList()
    # get_extension()
    # fetch_color()
    # get_examination_schedule()
    # list_methods()
    add_items_to_list()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
