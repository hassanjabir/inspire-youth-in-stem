#!/usr/bin/python

#####################
#   Arithmetic progression
#   Jabir Hassan
#   date: 23/5/2022
#####################

## a=First term 
##d=Common diffrence
##n=Number of terms

#a=int(input("enter the first number"))
d= int(input("enter the  coomon diffrence"))
#n=int(input("enter the number of terms"))
for i in range(1,n+1):
    n_term=a + a(i-1)*d
    #print(n_term)
sum_n = (n_term/2)*(2*a+(n-1)*d)
#print(sum_n)


