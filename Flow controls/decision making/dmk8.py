number_of_classes=int(input("number of classes"))
classes_attended=int(input("enter no: of classes attended"))
percentage=(classes_attended/number_of_classes)*100

if(percentage>75):
    print("will be allowed in exam hall",percentage)
else:
    print("will not be allowed")