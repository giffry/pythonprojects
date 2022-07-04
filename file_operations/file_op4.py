f=open("sample2","r")
lst=[]
even_list=[]
odd_list=[]
even_sum=0
odd_sum=0
for i in f:
    lst.append(int(i.rstrip("\n")))
print(lst)
print(sum(lst))
for i in lst:
    if(i%2==0):
        even_list.append(i)
    else:
        odd_list.append(i)
print(even_list)
print(odd_list)
print(sum(even_list))
print(sum(odd_list))
