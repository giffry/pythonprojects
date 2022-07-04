#master_string="abbcddeghgggt"
#chk_word=egg

master_string="abbcddeghgggt"
chk_word="egg"

res=""

dic={}

for char in master_string:
    if char in dic:
        dic[char]+=1
    else:
        dic[char]=1

for char in chk_word:
    if char in chk_word:
        curr_count=dic.get(char)
        if curr_count>0:
            res+=char
            dic[char]-=1
        else:
            break

print(res)
