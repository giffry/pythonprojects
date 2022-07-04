class Course:
    def addcourse(self,**kwargs):
        self.course_name=kwargs.get("course_name")
        self.status=kwargs.get("status")

    def __str__(self):
        return self.course_name

class Batch:
    def Addbatch(self,**kwargs):
        self.course=kwargs.get("course")
        self.batch_code=kwargs.get("batch_code")
        self.start_date=kwargs.get("start_date")

    def __str__(self):
        return self.batch_code

class Student:
    def addstudent(self,**kwargs):
        self.student_name=kwargs.get("student_name")
        self.email=kwargs.get("email")
        self.batch=kwargs.get("batch")

    def __str__(self):
        return self.student_name



django=Course()
django.addcourse(course_name="django",status="True")
ms=Course()
ms.addcourse(course_name="mearnstack",status="True")
bd=Course()
bd.addcourse(course_name="bigdata",status="True")

djb1=Batch()
djb1.Addbatch(course=django,batch_code="djmay2k22b1",start_date="22-6-2022")
mearn1=Batch()
mearn1.Addbatch(course=ms,batch_code="msapril2k22",start_date="22-8-2022")

arjun=Student()
arjun.addstudent(student_name="arjun",email="arjun@gmail.com",batch=djb1)

abhijith=Student()
abhijith.addstudent(student_name="abhijith",email="abhi@gmail.com",batch=djb1)

vishnu=Student()
vishnu.addstudent(student_name="vishnu",email="vishnu@gmail.com",batch=mearn1)

amal=Student()
amal.addstudent(student_name="amal",email="amal@gmail.com",batch=mearn1)


students=[]
students.append(arjun)
students.append(vishnu)
students.append(amal)

students=[std.student_name for std in students if std.batch.course.course_name=="mearnstack"]
print(students)