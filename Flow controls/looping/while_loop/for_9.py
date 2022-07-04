low=int(input("enter lower limit"))
upp=int(input("enter upper  limit"))

even_sum=0
odd_sum=0

for i in range(low,upp+1):
    if(i%2==0):
        even_sum+=i
    else:
        odd_sum+=i
print(even_sum)
print(odd_sum)