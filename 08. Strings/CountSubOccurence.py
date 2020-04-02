"""
19.11.2018 22:24
Count substring occurence in string
Bogdan Prădatu
"""

print("""This program will count the number of occurences of a substring
inside a given string\n""")
print("Use the function countSub(pattern,string) to do that")

def countSub(pattern, string):
    """ Count how many times the subtring 'pattern' occures in 'string'"""
    i = 0
    count = 0
    for char in string:
        start = i
        end = len(pattern)+i
        a = string[start:end]
        if a == pattern:
            count += 1
        i += 1
    return count

def test_countSub():
    test_string1 = "Mississippi"
    test_pattern1 = "is"
    test_string2 = "banana"
    test_pattern2 = "an"
    test_string3 = "banana"
    test_pattern3 = "ana"
    test_string4 = "banana"
    test_pattern4 = "nana"
    test_string5 = "aaaaaa"
    test_pattern5 = "aaa"
    test_string6 = ""
    test_pattern6 = "a"
    test_string7 = "aaaaaa"
    test_pattern7 = "b"
    test_string8 = "ala bala portocala"
    test_pattern8 = "al"

    if (countSub(test_pattern1,test_string1) == 2 and
        countSub(test_pattern2,test_string2) == 2 and
        countSub(test_pattern3,test_string3) == 2 and
        countSub(test_pattern4,test_string4) == 1 and
        countSub(test_pattern5,test_string5) == 4 and
        countSub(test_pattern6,test_string6) == 0 and
        countSub(test_pattern7,test_string7) == 0 and
        countSub(test_pattern8,test_string8) == 3):
        print("\nTest OK!")
    else:
        print("\nTest failed!")

test_countSub()
