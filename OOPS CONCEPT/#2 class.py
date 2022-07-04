#class

class Person:
    def printa(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printval(self):
        print(self.name,self.age,self.place)

class Student(Person):
    def printb(self,roll,department):
        self.roll=roll
        self.department=department
    def printsta(self):


        print(self.name,self.age,self.place,self.roll,self.department)

st=Student()
st.printa("anju",25,"kochi")
st.printb(101,"civil")
st.printsta()

