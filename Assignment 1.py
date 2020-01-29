# Programmer: Yaritza Torres-Rivera
# Course: CS151, Dr. Simari
# Date: January 29, 2020
# Programming Assignment: 1
# Program Inputs: lenght, width, and height. (float)
# Program Outputs: Number of gallons prime and paint. (integer)
import math

# output porpuse
print("This program will tell us the amount prime and paint in gallons that is need to cover the room, based on the area of the entire room, except the floor. ")

# ask user for area of the room input (length*width*height) (float)
lenght = input ("Please enter the room's length in feet: ")
lenght = float (lenght)
width = input ("Please enter the room's width in feet: ")
width = float (width)
height = input ("Please enter the room's height in feet: ")
height = float (height)

# compute the total area painted. (float)
area_painted = (2*(lenght*height)+2*(width*height)+(lenght*width))
area_painted = float (area_painted)

# compute the amount of prime in gallons. (one Gallon covers 200 square feet)(round)
amount_of_prime = area_painted / 200
amount_of_prime = round (amount_of_prime)

# compute the amount of paint in gallons. (One Gallon covers 325 squre feet)(round)
amount_of_paint = area_painted / 350
amount_of_paint = round (amount_of_paint)

# output number of prime gallons.
print ("Amount of prime needed in gallons is: ", amount_of_prime)

# output number of paint gallons.
print ("Amount of paint needed in gallons is: ", amount_of_paint)

# output total area of room painted. (float)
print ("The area of the room that is going to be painted is: ", area_painted)
