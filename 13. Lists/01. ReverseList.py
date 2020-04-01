'''
18.10.2018 17:34
Reverse list elements order
'''

list1 = [0,1,2,3,4,5,6,7,8,9]

def rev():
    list2 = []
    for i in list1:
        list2.append(list1[len(list1)-1-i])
    return list2

rev()
print(list1)
print(rev())
