given_string = input("Enter the string:- ")


def manipulate_string(given_string):
        if len(given_string) >= 2 and (given_string[:2] == "Is" or
                given_string[:2] == "is"):
            return given_string
        return "Is " + given_string

print(manipulate_string(given_string))

