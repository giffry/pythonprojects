#nested list

lst=[[101,'arun','k',26,'bigdata',1000],
     [102,'arjun','p',25,'python',1500],
     [103,'appu','l',24,'python',1000],
     [104,'aravind','j',29,'bigdata',2000],
     [105,'anas','h',22,'python',1800]]






# for i in lst:
#      print(i[1],i[2],i[3],i[4],)

# for i in lst:
#      if(i[3]>25):
#           print(i[1],i[2],i[3],i[4])

# for i in lst:
#      if(i[4]=='python'):
#           print(i[1],i[2],i[3],i[5])

# for i in lst:
#      if((i[5]>1750) and i[3]>25):
#           print(i[1:6])

sum=0
for i in lst:
     sum+=i[5]
print(sum)     

