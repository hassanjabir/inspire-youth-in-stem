#!/usr/bin/python

#####################
#   quadratic equations
#   Jabir Hassan
#   date: 31/5/2022
#####################
import math
a=int(input("enter the coefficient of the first term"))
b=int(input("enter the coefficient of the second term"))
c=int(input("enter the constant(c)"))
w= math.sqrt(b**2)-4*a*c




def find_root (a,b,c):
    y_1=-b+math.sqrt(b**2)-(4*a*c) /(2*a)
    y_2=(-b+w)/(2*a)
    y_2=(-b+w)/(2*a)

    print("the roots of the quadratic equation are",y_1,y_2)
find_root(a,b,c)

    

