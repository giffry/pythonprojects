dic={"name":'ajith',"age":25,'prof':"bigdata",'salary':5000}
print(dic)

print(dic['prof'])
if('company' in dic):
    pass
else:
    dic['company']="luminar"

dic["salary"]+=5000

for i in dic:
    print(i,dic[i])
