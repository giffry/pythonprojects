#regular expressions
#......................

#...a package used in python(...used for pattern matching)

import re
s="abaaabbbbabaaaabab"
count=0

#finditer(argument1,argument2)

#argument1:  find pattern
#argument2:  string name

matcher=re.finditer('ab',s)

for i in matcher:
    count+=1
    print(i.start())      #.....(to print the index values of the pattern)
print(count)