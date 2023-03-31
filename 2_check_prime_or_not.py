# write   a python program to create a function that takes a number as a parameter and checks if the number is prime or not.

def checkPrime(num):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                return "not Prime"
        else:
            return "prime"
    return "not prime"
print(checkPrime(-5))