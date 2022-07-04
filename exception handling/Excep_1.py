num1=int(input("enter number1"))
num2=int(input("enter number2"))
# div=num1/num2
# print(div)
#.....errors occurs due to value of input and excep handl is used to resolve it.

#..3 blocks

#try    :exception varan chance ulla code try blockil define cheyyam
#except  :code to resolve exception is mentioned here
#finally  :it will work everywhere eventhough there is exception or not


try:
    print(num1/num2)
except:
    print("zero division error")

