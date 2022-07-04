f=open("C:/Users/moham/Downloads/customer","r")
dic={}
for i in f:
    data=i.rstrip("\n").split(",")

    proff=data[4]

    if proff not in dic:
        dic[proff]=1
    else:
        dic[proff]+=1
print(dic)

# if(data[3]>'50' and data[-1]=="india"):
#     print(data[1:-1])

# if(data[3]>"50"):
#         print(data[1:5])
#each preffession count

