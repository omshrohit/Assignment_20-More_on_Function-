# write a python program  to access a function inside a function.

def sqr(num):
    return num**2

def cube(num):
    return num*sqr(num)

print(cube(5))