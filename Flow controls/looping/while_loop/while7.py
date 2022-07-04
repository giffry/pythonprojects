#print even numbers between lower and upper limits

low=int(input("enter lower limit"))
upp=int(input("enter upper limit"))

while(low<=upp):
    if(low%2==0):
        print(low)
    low+=1
