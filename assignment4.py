#!/usr/bin/python 

#####################
#   loops: for loops
#   Jabir Hassan
#   date: 23/5/2022
#####################



#create a list of cars


cars=["audi","mazda","ferari","jeep","mecedes"]

#using a for loop to print all cars

for car in cars:
    print(car.title())
    if car=="jeep":
        print(car.upper())
