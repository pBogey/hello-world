"""
07.01.2018 19:36
Find function for string
Bogan Prădatu - from how to think like a computer scientist
"""


def find(strg, ch, start=0, end=0):
    index = start
    if end == 0:
        end = len(strg)
    while index < end:
        if strg[index] == ch:
            return index
        index += 1
    return -1
