class Person:
    def seta(self,name,age):
        self.name=name
        self.age=age
    def printa(self):
        print(self.name,self.age)

class Child(Person):
    def setb(self,place,school):
        self.place=place
        self.school=school
    def printb(self):
        print(self.place,self.school)

class Student(Child):
    def setc(self,roll,dept,college):
        self.roll=roll
        self.dept=dept
        self.college=college
    def printc(self):
        print(self.name,self.age,self.place,self.dept,self.college)

st=Student()
st.seta("akash",25)
st.setb("kochi","abcd")
st.setc(101,"python","sngss")
st.printc()

