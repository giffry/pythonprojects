#static variable....

class Luminar:
    inst_name="luminar"
    fees="29500"
    def setvalue(self,name,age):
        self.name=name
        self.age=age

    def printvalue(self):
        print(self.name,self.age,Luminar.inst_name,Luminar.fees)

lm=Luminar()
lm.setvalue("aruna",23)
lm.printvalue()

lm1=Luminar()
lm1.setvalue("athil",25)
lm1.printvalue()

lm2=Luminar()
lm2.setvalue("bibin",29)
lm2.printvalue()