f=open("sample2","r")
lst=[]
for i in f:
    lst.append(int(i.rstrip("\n")))
print(lst)
print(sum(lst))


#rstrip


