f=open("demofile","r")
special="@#$%^&*()"
for i in f:
    data=i.rstrip("\n")
    string1=""
    for j in data:
        if j not in special:
            string1+=j
    print(string1)






