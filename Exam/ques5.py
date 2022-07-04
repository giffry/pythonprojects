#12345
#22345
#33345
#44445
#55555

for i in range(1,6):
    for j in range(1,6):
        if j<i:
            print(i,end=' ')
        else:
            print(j,end=' ')
    print()
