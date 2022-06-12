#!/usr/bin/python

#####################
#   functions
#   Jabir Hassan
#   date: 2/6/2022
#####################

## return from a function

def get_sum(num1,num2):
    sum_nums = num1 + num2
    return sum_nums

print(get_sum(7,12))

### square of numbers

def powers (number,power):
    power_numb = number**power
    return power_numb
powers(6,4)
print(powers)

def get_full_name(f_name , s_name):
    full_name = f_name + "" + s_name
    return full_name.title()
print(get_full_name("hassan","jabir"))


## returning a dictionary from a function

def create_full_name(f_name,s_name):
    person = { 'first name': f_name,'second name':s_name}
    return person

student = create_full_name('hassan','jabir')
print(student)

## passing a list in a function

def greet_friends(names):
    for name in names:
        msg =    "  hello  "   +   name.title() +    "!"
        print  (msg)

friends = [ 'njugush', 'moha', 'richie', 'fatuma']
greet_friends (friends)

