#read lower and upper limit
#sum of even numbers between them
#sum of odd numbers between them

low=int(input("enter lower limit"))
upp=int(input("enter upper limit"))

even_sum=0
odd_sum=0

while(low<=upp):
    if(low%2==0):
        even_sum+=low
    else:
        odd_sum+=low
    low+=1
print("sum of even numbers=",even_sum)
print("sum of odd numbers=",odd_sum)