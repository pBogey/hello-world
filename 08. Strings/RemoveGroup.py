"""
16.12.2018 01:32
Remove a group of letters from a string
Bogdan Prădatu
"""


print("This program will remove a group of letters from a string")
# Input the initial text in the first line,
# then go to a new line and input the group of letters you would like removed.

string1 = input("\nEnter your text:")
group = input("Enter the group of letters you want removed:")


def remove_group(string, group):
    """Removes a 'group' of letters from a given 'strring'"""
    string2 = string.split(group)
    string2 = "".join(string2)
    return string2


print("\nInitial text:", string1)
print("Processed text:", remove_group(string1, group))
