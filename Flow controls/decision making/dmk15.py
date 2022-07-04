cost=int(input("enter the cost"))

tax=0

if(cost>100000):
    print("tax=",cost*0.15)

elif(cost>50000<=100000):
    print("tax=",cost*0.10)

elif(cost<=50000):
    print("tax=",cost*0.05)

else:
    print("not applicable")