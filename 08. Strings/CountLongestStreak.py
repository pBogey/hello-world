"""
05.02.2020
Find the longest alphabetical streak in a string and print it
Bogdan Prădatu
"""


def test_longest_alpha_substring():
    assert(longest_alpha_substring('') == '')
    assert(longest_alpha_substring('a') == 'a')
    assert(longest_alpha_substring('aa') == 'a')
    assert(longest_alpha_substring('abc') == 'abc')
    assert(longest_alpha_substring('azbycx') == 'az')
    assert(longest_alpha_substring('abcdefghijcsdferq') == 'abcdefghij')
    print("Test OK")
    return 1


def longest_alpha_substring(s: str) -> str:
    """
    :param s: target string
    :return: longest substring of alphabetically arranged characters
    """
    if s:
        result = s[0]
    else:
        return ""
    for i in range(len(s)):
        substring = s[i]
        for j in range(i, len(s)-i-1):
            if s[j] < s[j+1]:
                substring += s[j+1]
                if len(result) < len(substring):
                    result = substring
            else:
                substring = s[j+1]
    return result


test_longest_alpha_substring()
