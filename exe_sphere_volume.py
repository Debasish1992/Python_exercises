import math
radius = int(input("Enter sphere radius:- "))
volume = 4/3 * 3.14 * radius * radius
volume = math.ceil(volume)
print("The Sphere radius is {volume} ".format(volume = volume))