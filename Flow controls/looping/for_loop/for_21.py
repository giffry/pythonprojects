#read a lower limit and upper limit
#print prime numbers between lower and upper limits

low=int(input("enter the lower limit"))
upp=int(input("enter the upper limit"))


for num in range(low,upp+1):
    for i in range(2,num):
        if(num%i==0):
            break
    else:
        print(num)


