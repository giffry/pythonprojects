f=open("C:/Users/moham/Downloads/temper","r")
dic={}
for i in f:
    data=i.rstrip("\n").split(",")
    dis=data[0]
    tem=data[1]
    if dis not in dic:
        dic[dis]=tem
    else:
        old_tem=dic[dis]
print(dic)