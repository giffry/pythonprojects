#...........

class Person:
    def __init__(self):
        self.name="arjun"
        self._salary=5000
        self._age=26
    def printval(self):
        print("Iam in the class person")
        print(self.name)
        print(self._salary)
        print(self._age)
class Employee(Person):
    def __init__(self):
        Person.__init__(self)
    def printval2(self):
        print("Iam in employee class")
        print(self.name)
        print(self._salary)
        print(self._age)

ob=Employee()
ob.printval()
ob.printval2()

