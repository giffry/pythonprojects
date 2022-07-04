lst=[4,1,5,3,9,12]

lst.sort()
print(lst)
num=int(input("enter a number"))
low=0
upp=len(lst)-1
mid=0
mid=(low+upp)//2
flag=0

while(low<=upp):
    mid=(low+upp)//2
    if(num>lst[mid]):
        low=mid+1
    elif(num<lst[mid]):
        upp=mid-1
    elif(num==lst[mid]):
        flag=1
        break
if(flag>0):
    print("element found")
else:
    print("not found")


