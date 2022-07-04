#multilevel inheritance
#............

class A:
    def seta(self):
        print("inside class A")

class B(A):
    def setb(self):
        print("inside class B")

class C(B):
    def setc(self):
        print("inside class C")

ob=C()
ob.setb()
ob.seta()