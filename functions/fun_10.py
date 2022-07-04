#method3
def fact(num1):
    fac=1
    for i in range(1,num1+1):
        fac=fac*i
    return fac

data=fact(5)
data2=fact(6)
print(data)
print(data2)