class Employee:
    def setvalue(self,name,id,desig,salary,company):
        self.name=name
        self.id=id
        self.desig=desig
        self.salary=salary
        self.company=company
    def printvalue(self):
        print(self.name,self.id,self.desig,self.salary,self.company)

emp1=Employee()
emp1.setvalue("anju",123,"manager",50000,"logitech")
emp1.printvalue()

emp2=Employee()
emp2.setvalue("arjun",29,"lead",25000,"luminar")
emp2.printvalue()

emp3=Employee()
emp3.setvalue("appus",28,"hr",40000,"infotech")
emp3.printvalue()
