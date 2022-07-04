sub1=int(input("enter sub1 mark"))
sub2=int(input("enter sub2 mark"))
sub3=int(input("enter sub3 mark"))
sub4=int(input("enter sub4 mark"))

score=(sub1+sub2+sub3+sub4)

if(score>=180):
    print("grade A+")
elif(score>=160<180):
    print("A grade")
elif(score>=140<160):
    print("B+ grade")
elif(score>=120<140):
    print("B grade")
elif(score>=100<120):
    print("C+ grade")
elif(score>=80<100):
    print("C grade")
else:
    print("failed")