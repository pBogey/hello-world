'''
18.11.2018 21:54
Removes letters from strings
Bogdan Prădatu
'''

print("This program will remove the elements of a string \n")

string1 = input("Enter your text: ")
character = input("Enter letter you want removed: ")

def remove_char(char,string):
    """Removes a character from a given string."""
    string2 = ""
    i = 0
    for c in string:
        if c != char:
            string2 += string[i]
        i += 1
    return string2

print(string1)
print(remove_char(character,string1))

def test_remove():
    test_string1 = "apple"
    test_string2 = "banana"
    test_string3 = ""
    test_string4 = "a"

    if (remove_char("a",test_string1) == "pple" and
        remove_char("a",test_string2) == "bnn" and
        remove_char("z",test_string2) == "banana" and
        remove_char("a",test_string3) == "" and
        remove_char("b", test_string4) == "a"):
        print("\n\nTest ok!")
    else:
        print("\n\nTest failed")

test_remove()
