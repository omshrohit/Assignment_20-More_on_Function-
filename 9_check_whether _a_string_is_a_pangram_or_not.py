# write  a python program to create  a function to check whether a string  is a pangram or  not.
def  checkpangram(string):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    string1=string.lower()
    for ch in alphabet:
        if ch not in string1:
            return "not pangram"
    else:
        return "pangram"
res=checkpangram("abcdefghijklmnop qrs tuv Wxyz")
print(res)