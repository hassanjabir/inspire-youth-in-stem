#!/usr/bin/python

#####################
#   factorials
#   Jabir Hassan
#   date: 27/5/2022
#####################
 
number= int(input("enter the number"))

factorial = 1
if (number)<0:
    print("factorial of negative numbers does not exist")
elif number ==0:
    print("factorial of 0 is equal to one")
else:
    for  i in  range(1,(number) + 1):
        factorial = factorial * i
print("factorial of number",factorial)


