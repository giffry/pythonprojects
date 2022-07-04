#woedcount
#.............

#split-fun used to convert line of data into word by word data

Line='rat rat cat cat car bat bus bus'

data=Line.split(' ')
print(data)
dic={}

for i in data:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
print(dic)        
