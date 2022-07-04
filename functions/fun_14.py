#create a calculator

#1 addition
#2 substraction
#3 multiplication
#4 division

def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def mult(num1,num2):
    return num1*num2

def div(num1,num2):
    return num1/num2

print("select your choice \n")
print("1.addition \n")
print("2.substraction \n")
print("3.multiplication \n")
print("4.division \n")

choice=input("select operation form 1,2,3,4:")
num1=int(input("enter first number"))
num2=int(input("enter second number"))

if choice=="1":
    print(num1,"+",num2,"=",add(num1,num2))

elif choice=="2":
    print(num1,"-",num2,"=",sub(num1,num2))

elif choice=="3":
    print(num1,"*",num2,"=",mult(num1,num2))

elif choice=="4":
    print(num1,"/",num2,"=",div(num1,num2))
else:
    print("invalid input")



