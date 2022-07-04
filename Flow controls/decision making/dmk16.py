num1=int(input("enter number1"))
num2=int(input("enter number2"))
num3=int(input("enter number3"))

if(num1>num2)&(num1>num3):
    if(num2>num3):
        print("second largest is",num2)
    else:
        print("second largest num is",num3)
elif(num2>num1)&(num2>num3):
    if(num1>num3):
        print("second largest is",num1)
    else:
        print("second largest is",num3)
elif(num3>num1)&(num3>num2):
    if(num1>num2):
        print("second largest number is=",num1)
    else:
        print("second largest num is",num2)
else:
    print("invalid")

