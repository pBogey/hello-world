"""
27.12.2018 11:42
Remove Duplicates from sequence
Bogdan Prădatu
"""

test_list = [0, 4, 5, 4, 3, 7, 8, 45, 3, 4, 23, 3, 15, 32, 5, 7, 32, 0, 1, 9, 3, 23]


def remove_duplicates(lst):
    """Return a list with duplicates removed from "lst" """
    lst1 = []
    for i in lst:
        if i in lst1:
            continue
        else:
            lst1.append(i)
    # lst = lst1
    return lst1


print(test_list)
print(remove_duplicates(test_list))
