#!/usr/bin/python

#####################
#   opeations
#   Jabir Hassan
#   date: 6/6/2022
#####################

import operations
from student import student
operations.add_numbers(3,5)
operations.mult_numbers(100,2)
operations.sub_numbers(40,3)
operations.div_numbers(4,2)
print(operations.add_numbers)
print(operations.mult_numbers)
print(operations.sub_numbers)
print(operations.div_numbers)

from student import student
import student

new_student = student("jabir,playing football,"+str(2003))

student.greet_student()
print(student)


from teachers import Teachers

new_teacher = Teachers("Mr JOhn , 123456 , Biology, 400000")
print(new_teacher.get_tsc_no())




