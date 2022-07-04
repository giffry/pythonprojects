pattern='ABCDBCDEF'
dic={}

for i in pattern:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
        print(i,"first recursive character")
        break
print(dic)
