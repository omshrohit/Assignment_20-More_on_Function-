# write a python program to create a function that accepts a string and  calculate the number of upper case letter and lower case letters
def countUpperAndLower(name):
    countLower=0
    countUpper=0
    for i in  name:
        if ord(i)>=97 and ord(i)<=122:
            countLower+=1
        if ord(i)>=65 and ord(i)<=90:
            countUpper+=1
    print(f"number of lower letter :{countLower}\nnumber of upper letter :{countUpper}")
countUpperAndLower("Hello World")