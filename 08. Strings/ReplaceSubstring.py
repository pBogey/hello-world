"""
16.12.2018
Replace substring in string
Bogdan Prădatu
"""

print("""This program will replace a grup of letters within a string\n""")
print("Use the function replace_sub(string,old,new) to do that")

def replace_sub(string, old, new):
    """ replace "old" substring with "new" subtring within "string" """
    string2 = string.split(old)
    string2 = new.join(string2)
    return string2

print(replace_sub("Hello World!","Hello","Jellow"))
print(replace_sub("Bogdan","gd","AA"))
print(replace_sub("Mississippi","i", "I"))
