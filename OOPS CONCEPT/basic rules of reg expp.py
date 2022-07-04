#basic rules..........

import re
count=0
rule='[abc]'

matcher=re.finditer(rule,'abc@sabir123')

for i in matcher:
    count+=1
    print(i.group())
    print(i.start())
print(count)