# write a python program to create a function  that checks whether  a passed string is palindrome  or not.
def checkPalindrome(var1):
    if var1==var1[::-1]:
        return "palindrome"
    else:
        return "Not palindrome"
res=checkPalindrome("abcba")
print(res)
