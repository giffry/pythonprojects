# lst=[]
# for i in range(1,101):
#     lst.append(i)
# print(lst)

# lst=[i for i in range(1,101)]
# print(lst)

# lst=[i for i in range(1,76,4)]
# print(lst)

# lst=[i for i in range(1,101) if(i%2==0)]
# print(lst)

# lst=[i for i in range(1,51) if(i%2!=0)]
# print(lst)

lst=[(i,"even") for i in range(1,51) if(i%2==0)]
print(lst)

#syntax

#[print if condition else print range]

#[print1 if condition1 else print2 if condition2 else print3 range]