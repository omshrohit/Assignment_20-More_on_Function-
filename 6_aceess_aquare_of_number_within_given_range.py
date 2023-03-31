# write a python program to create a function  and print a list where the values are square of numbers between 1 and 30
def square(list1):
    list2=[]
    for  i in  range(len(list1)):
       for j in range(i+1,len(list1)):
           if list1[i]**2==list1[j]:
               list2.append(list1[j])
    print(list2)
square([e for e in range(1,31)])