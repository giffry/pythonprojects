#create a list from element of a range from 1200 to 2000 with steps of 130
#  lst=[44,54,64,74,104]
#   lst1=[50,60,70,80,110]
# 1,15  [elements square greater than 50]

 #1

# lst=[i for i in range(1200,2001,130)]
# print(lst)

#3
#
# lst=[i for i in range(1,16) if i**2>50]
# print(lst)

#2
# lst1=[44,54,64,74,104]
# lst2=[i+6 for i in lst1]
# print(lst2)

# dic={"sedan":1500,"suv":2000,"pickup":2500,"minivan":1600,"van":2400,"semi":13600}
# lst=[i.upper() for i in dic if dic[i]>2000]
# print(lst)

#1
# lst=[i for i in range(1,1001) if i%7==0]
# print(lst)

#2

# lst=[i for i in range(1,1001) if '3' in str(i) ]
# print(lst)

#3

line="Yellow Yaks like yelling and yawning and yesterday they yodled while eating yuky yams"
count=0
lst=[]
for i in line:
    if(i.isspace()):
        count=count+1
print(count)

#2





