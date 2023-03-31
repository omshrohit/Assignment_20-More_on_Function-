#  write a python program to create a function  to find the min    of  three numbers.
def minvalue(num1,num2,num3):
    if num1>num2 and num1>num3:
        return num1
    elif num2>num1 and num2>num3:
        return num2
    else:
        return num3
print(minvalue(10,-534,23))