# write a python program  to create a function that takes a list and return a nuw list with the original list's unique elements
def newlist(list1):
    list2=[]
    j=0
    for i in list1:
        if j==list1.index(i):
            list2.append(i)
        j+=1
    return list2
newlist1=newlist([1,1,2,4,5,2,4,3])
print(newlist1)

# another method is
'''
print("another way")
def newlist1(list1):
    list2=list(set(list1))
    return list2
res=newlist1([1,1,2,4,5,2,4,3])
print(res)
'''