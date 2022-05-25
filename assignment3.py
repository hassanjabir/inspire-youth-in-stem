#write a program that gets the user input and adds ksh.to her acc if she is btwn 25-30 yrs

from cgi import print_environ


age= input("what is your age")

acc_bal=0

if (int(age) > 25) and  (int(age) < 30):
    acc_bal = acc_bal + 10000
    print("confirm you have received 10000")
else:
    print("sorry no money for you look for your own cash")

acc_bal =("enter your acc bal")

acc_bal=input("enter your acc_bal")
if(int(acc_bal)> 100000 and int(acc_bal)< 200000):
    acc_bal = acc_bal - 25000
    print("we have deducted ksh 25000")
elif (int(acc_bal) > 500000 and int(acc_bal), 1000000):
    acc_bal= int(acc_bal) -(0.3*int(acc_bal))
    print("we have deducted 30 percent from your account")
elif int(acc_bal) > 1000000:
    acc_bal = acc_bal - 15000
    print("we have deducted 15000 from your account")
     

    
      
     