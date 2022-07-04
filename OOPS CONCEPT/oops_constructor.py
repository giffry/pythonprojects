#CONSTRUCTOR....
#constructor-to define instance variable in the object we use constructor

class Person:
    def __init__(self,name,age,place):  #...__init__ is the constructor
        self.name=name
        self.age=age
        self.place=place

    def printvalue(self):
        print(self.name,self.age,self.place)

pe1=Person("chandran",28,"kochi")
pe1.printvalue()
