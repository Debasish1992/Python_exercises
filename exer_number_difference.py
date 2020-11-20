target_number = 17
result = 0
input_number = int(input("Enter the number:- "))
if input_number > target_number:
    result = 2 * (input_number - target_number)
else:
    result = input_number - target_number

print("The difference is {result} ".format(result=result))
