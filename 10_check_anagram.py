# write a python script to create a function to check  whether a string is an anagram or not.
def anagram(var1,var2):
    for ch in  var1:
        if ch not  in var2:
            return "not anagdram"
    else:
        return "anagram"
print(anagram("abcd",'dcab'))