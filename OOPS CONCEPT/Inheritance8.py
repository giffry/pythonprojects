class Employee:
    def __init__(self,id,fname,lname,age,proff,country):
        self.id=id
        self.fname=fname
        self.lname=lname
        self.age=age
        self.proff=proff
        self.country=country

    def printemp(self):
        print(self.id,self.fname,self.lname,self.age,self.proff,self.country)

f=open("C:/Users/moham/Downloads/customer","r")
lst=[]
for i in f:
    data=i.rstrip("\n").split(",")
    lst.append(i)
    print(lst)    
    # ob=Employee(data[0],data[1],data[2],data[3],data[4],data[-1])
    # ob.printemp()