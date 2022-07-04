#multiple inhertance.............
#.................

#child inherits features of more than one parent class

class A:
    def printa(self):
        print("inside class A")

class B:
    def printb(self):
        print("inside class B")

class C(A,B):
    def printc(self):
        print("inside class C")

ob=C()
ob.printc()
ob.printb()
ob.printa()
