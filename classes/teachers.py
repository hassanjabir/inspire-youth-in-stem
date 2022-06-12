#!/usr/bin/python

#####################
#   opeations
#   Jabir Hassan
#   date: 6/6/2022
#####################


from unicodedata import name


class Teachers():
    def __init__(self,name,tsc_no,subject,salary):
     self.name = name
     self.tsc_no = tsc_no
     self.subject = subject
     self.salary = salary

def get_tsc_no(tsc_no):
    return tsc_no