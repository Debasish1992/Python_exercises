# Function responsible with passed data and default value
def print_data(first_name, last_name="Das"):
    return first_name + " " + last_name


# Function with unknown number of parameters
def unknown_function(*kids):
    print("The Youngest child is " + kids[2])


# Default value with function
def default_value_function(country="Norway"):
    print("I am from " + country)


def my_function():
    pass


default_value_function("America")
default_value_function("India")
default_value_function()
full_data = print_data("Debasing")
unknown_function("Test", "Data", "Test Data")
print(full_data)
my_function()
