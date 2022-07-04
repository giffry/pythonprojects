class Person:
    def setvalue(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printvalue(self):
        print(self.name)
        print(self.age)
        print(self.place)

pe=Person()
pe.setvalue("aravind",25,"wayanad")
pe.printvalue()

pe1=Person()
pe1.setvalue("rakesh",28,"kochi")
pe1.printvalue()




