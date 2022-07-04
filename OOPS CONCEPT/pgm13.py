employee=['vinay','anu']
default={"designation":'bigdata',"salary":1000}

#fromkeys : it returns with a specified keys and specified values

res=dict.fromkeys(employee,default)
print(res)

print(res['vinay'])