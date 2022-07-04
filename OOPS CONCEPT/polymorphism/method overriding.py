class Add:
    def sum(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print("inside class A",self.num1+self.num2)

class Add2(Add):
    def sum(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print("inside class B",self.num1+self.num2)

#SAME METHOD NAME AND SAME NO: OF ARGUMENTS.....THIS IS METHOD OVERRIDING

ob=Add2()
ob.sum(15,20)

#HERE CHILD CLASS OVERWRITES PARENT CLASS


