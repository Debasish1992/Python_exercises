def check_for_vowel():
    given_character = input("enter the character")
    if given_character == "a" or given_character == 'e' or given_character == 'i' or given_character == 'o' or given_character == 'u':
        return True
    return False


if check_for_vowel():
    print("This is a vowel")
else:
    print("This is not a vowel")
