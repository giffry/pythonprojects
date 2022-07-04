class Student:
    def setvalue(self,name,roll_no,department,college_name):
        self.name=name
        self.roll_no=roll_no
        self.department=department
        self.college_name=college_name
    def printvalue(self):
        print(self.name)
        print(self.roll_no)
        print(self.department)
        print(self.college_name)

st1=Student()
st1.setvalue("abijith",1,"electronics","luminar")
st1.printvalue()

st2=Student()
st2.setvalue("giffry",24,"python","model")
st2.printvalue()

st3=Student()
st3.setvalue("bipin",45,"bigdata","sngc")
st3.printvalue()