#..............

import re

g="rossssrossssssrosrossssro"
count=0


matcher=re.finditer('ro',g)


for i in matcher:
    count+=1
    print(i.start())
print(count)
