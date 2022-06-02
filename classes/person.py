#!/usr/bin/python

#####################
#   classes
#   Jabir Hassan
#   date: 2/6/2022
#####################



class person:
    def __init__(self,_name,_age):
     self.name= _name
     self.age= _age

    def sayHi(self):
        print("hello, my name is "+self.name + " i am "+ (self . age))

person_1 =person("bob",str(16))
person_1.sayHi()


person_2 =person("jabir", str(22))
person_2.sayHi()


