low=int(input("enter lower limit"))
upp=int(input("enter upper limit"))

even_count=0
odd_count=0
for i in range(low,upp+1):
    if(i%2==0):
        even_count+=1
    else:
        odd_count+=1
print("number of even numbers",even_count)
print("number of odd numbers",odd_count)
