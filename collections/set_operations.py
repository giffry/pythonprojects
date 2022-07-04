#set operations......

#1...union      #combined elements of both sets...duplicate values wont be present
#2...intersection
#3...difference

#Union.....

st={10,12,14,16,20}
st1={11,13,10,16,20}
# st2=st.union(st1)
# print(st2)

#intersection.....

# st2=st.intersection(st1)
# print(st2)

#difference.....   # element present in set A not in set B

# st2=st.difference(st1)
# print(st2)

st2=st1.difference(st)
print(st2)






