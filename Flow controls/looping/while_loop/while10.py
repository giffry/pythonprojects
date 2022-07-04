#reverse
# #153
num1=int(input("enter  a number"))
res=0

while(num1!=0):
    dig=num1%10
    res=(res*10)+dig
    num1=num1//10
print(res)





