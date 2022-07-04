#multiplication table of a given number

num1=int(input("enter a number"))

i=1
while(i<=10):
    res=(i*num1)
    print(i,"*",num1,"=",res)
    i+=1