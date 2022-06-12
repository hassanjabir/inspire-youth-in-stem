#!/usr/bin/python

#####################
#   Arithmetic progression
#   Jabir Hassan
#   date: 23/5/2022
#####################

a= int (input("enter first term"))
d= int(input("enter common diffrence"))
n= int(input("enter number of terms"))


for i in range (1 , n + 1):
    n_terms = a + d * (i-1)
    print(n_terms)

s_n = float((n/2)*(2*a+(n-1)*d))
print(s_n)



