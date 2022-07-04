# lst=[4,3,2,1]
# num=int(input("enter a number"))
#
# for i in lst:
#     for j in lst:
#         if(i+j==num):
#             print(i,"+",j,"=",num)
#         else:
#             print("invalid")

lst=[4,3,2,1]
lst.sort()

num=int(input("enter a number"))
low=0
upp=len(lst)-1

while(low<=upp):
    data=lst[low]+lst[upp]

    if(data==num):
        print("pairs are",lst[low],lst[upp])
        break
    elif(data>num):
        upp=upp-1
    else:
        low=low+1


