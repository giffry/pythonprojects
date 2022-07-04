#check given num is prime or not

num1=int(input("enter a number"))
flg=0

for i in range(2,num1):
    if(num1%i==0):
        flg=1
        break
if(flg>1):
    print("not prime")
else:
    print("prime")


