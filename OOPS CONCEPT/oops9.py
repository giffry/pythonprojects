#class person   name,age
#parent         place,ph no:
#employee       id,desig,salary

class Person:
    def printa(self,name,age):
        self.name=name
        self.age=age
    def printval(self):
        print(self.name,self.age)

class Parent:
    def printb(self,place,phone_no):
        self.place=place
        self.phone_no=phone_no
    def printpar(self):
        print(self.place,self.phone_no)

class Employee(Person,Parent):
    def printc(self,id,desig,salary):
        self.id=id
        self.desig=desig
        self.salary=salary
    def printemp(self):
        print(self.name,self.age,self.place,self.phone_no,self.id,self.desig,self.salary)

ob=Employee()
ob.printa("appu",25)
ob.printb("ernakulam",123456)
ob.printc(101,"bigdata",1000)
ob.printemp()
