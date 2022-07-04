student=[('vinay',45),('arjun',35),('amal',65),('vipin',56)]

#highest mark name to be printed

marks=[]

for i in student:
    marks.append(i[1])

maximum=max(marks)

for j in student:
    if j[1]==maximum:
        print(j[0])