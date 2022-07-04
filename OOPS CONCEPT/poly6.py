#class person-name,age,place
#employee  -id,dept,salary
#student    -roll,college

class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place


class Employee:
    def __init__(self,id,dept,salary):
        self.id=id
        self.dept=dept
        self.salary=salary


class Student(Employee,Person):
    def __init__(self,roll,college,name,age,place,id,dept,salary):
        Person.__init__(self,name,age,place)
        Employee.__init__(self,id,dept,salary)
        self.roll=roll
        self.college=college
    def printstudent(self):
        print(self.name,self.age,self.place,self.id,self.dept,self.salary,self.roll,self.college)

ob=Student("sachin",25,"ollur",12345,"python",25000,101,"cec")
ob.printstudent()

#CONSTRUCTOR IN MULTIPLE INHERITANCE