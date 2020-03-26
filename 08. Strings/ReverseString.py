'''
18.11.2018 20:07
Reverse string letters
'''

print("This program will reverse the elements of a string \n")

string1 = input("Enter your text: ")

def rev(string):
    """Reverses the order of elements of given string.
    String must be previously defined."""
    string2 = ""
    i = 0
    for w in string:
        string2 += string[len(string)-1-i]
        i = i + 1
    return string2

print(string1)
print(rev(string1))
print("\nMirror function: ", string1+rev(string1))

def test_rev():
    test_string1 = "happy"
    test_string2 = "Python"
    test_string3 = ""
    test_string4 = "a"

    if rev(test_string1) == "yppah" and rev(test_string2) == "nohtyP" and rev(test_string3) == "" and rev(test_string4) == "a":
        print("\n\nTest ok!")

test_rev()
