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

class Vehicle:

     def __init__(self,max_speed,mileage):

          self.max_speed= max_speed
          self.mileage= mileage

toyota = Vehicle('300km/hr,4000km')

print(toyota.max_speed,toyota.mileage)






