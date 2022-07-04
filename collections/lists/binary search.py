#binary_search
def binarysearch(lst,key):
    low=0
    high=len(lst)-1
    mid=0
    while(low<=high):
        mid=(low+high)//2
        if(lst[mid]<key):
            low=mid+1
        elif(lst[mid]>key):
            high=mid-1
        else:
            return mid
    return -1
lst=[4,7,9,12,13,14]
key=7
r=binarysearch(lst,key)
if(r==-1):
    print("not found")
else:
    print("found")

