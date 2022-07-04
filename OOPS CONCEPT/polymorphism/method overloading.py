class Add:
    def sum(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print(self.num1+self.num2)

class Add1:
    def sum(self,num1,num2,num3):
        self.num1=num1
        self.num2=num2
        self.num3=num3
        print(self.num1+self.num2+self.num3)

ob=Add1()

ob.sum(5,6,4)

#in python in this case the latest given method only works
#does not support method overloading in python