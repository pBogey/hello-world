"""
22.12.2018 02:09
Dictionary Sorting Algorithm
Bogdan Prădatu
"""


d1 = {"one": 1, "four": 4, "three": 3, "five": 5, "two": 2, "zero": 0,
      "six": 6, "ten": 10, "eight": 8, "nine": 9, "seven": 7}


# My sorting algorithm (edit: Bubble sorting, it seems)
def dict_sort(d, reverse=False):
    """Sort given dictionary in ascending (default)
        or descending (reverse = True) order"""
    key_list = list(d.keys())
    value_list = list(d.values())
    for j in range(len(value_list)-1):
        for i in range(len(value_list)-1):
            if not reverse:
                if value_list[i] > value_list[i+1]:
                    value_list[i], value_list[i+1] = value_list[i+1], value_list[i]
                    key_list[i], key_list[i+1] = key_list[i+1], key_list[i]
            elif reverse:
                if value_list[i] < value_list[i+1]:
                    value_list[i], value_list[i+1] = value_list[i+1], value_list[i]
                    key_list[i], key_list[i+1] = key_list[i+1], key_list[i]
    d = {}
    for i in range(len(value_list)):
        d[key_list[i]] = value_list[i]
    dict1 = d    
    return dict1


print("***** Sorting *****")
print(dict_sort(d1))
print("\n***** reverse Sorting *****")
print(dict_sort(d1, reverse=True))
