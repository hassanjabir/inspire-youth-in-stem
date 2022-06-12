#!/usr/bin/python

#####################
#   classes
#   Jabir Hassan
#   date: 2/6/2022
#####################

from sre_constants import SRE_FLAG_ASCII


class vehicle:
    def __init__(self,srl,max_speed,mileage):
       self.serial = srl
       self.max_speed = max_speed
       self.mileage = mileage


Bugatti = vehicle('0006','678km/h','6000')
print(Bugatti.max_speed,Bugatti.mileage)

def specs(self):
    print("vehicle serial no,"+ str(self.serial_no) + "has a maximum speed of "+ str(self.max_speed) + "and a mileage of " + " ,  ")

Bugatti = vehicle('0006','678km/h','6000')
Toyota = vehicle('0007','250km/h','700')
Bugatti.specs()