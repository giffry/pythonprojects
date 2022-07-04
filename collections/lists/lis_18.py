lst=[4,5,10,12,20]

#lst1=[47,46,41,39,31]
lst1=[]

total=sum(lst)

for i in lst:
    res=total-i
    lst1.append(res)
print(lst1)
