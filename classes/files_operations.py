#!/usr/bin/python

#####################
#   opeations
#   Jabir Hassan
#   date: 6/6/2022
##################



f = open("lessson.txt")
f = open("lessson1.txt","x")
#read line by line
f.readline()
print (f.readline())

with open("lesson1.txt","w",encoding= 'utf-8') as f :
    f.write("this is my first text file that has been created\n")
    f.write("i am from nakuru county and i currently reside in nairobi\n\n")
    f.write("today is a very chilly day amd people are clad in heavy clothing\n")

### reading the file
print(f.read())
f.close()
