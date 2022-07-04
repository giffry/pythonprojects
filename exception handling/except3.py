#identify

a=[1,2,3,4]
i=int(input("enter a index"))
try:
    print(a[i])
except Exception as e:
    print("error occured is",e)