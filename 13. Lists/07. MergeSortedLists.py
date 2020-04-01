"""
27.12.2018 12:10
Merge Sorted Lists: from how to think like a computer scientist 3rd edition
Bogdan Prădatu
"""

l1 = [0,1,2,3,4,5,6,7,8,9]
l2 = [10,11,12,13,14,15,16,17,18,19]

l3 = [0,2,4,6,8]
l4 = [1,3,5,7,9]

l5 = [0,10,14]
l6 = [5,12,15,16,17,18,19]


def merge(xs,ys):
    """Merge sorted lists xs and ys. Return a sorted result"""
    result = []
    xi = 0
    yi = 0
    print("Len xs:",len(xs),"\nLen ys:",len(ys))
    while True:
        if xi >= len(xs):               #If xs list is finished
            result.extend(ys[yi:])      #Add remaining items from ys
            print("*")
            return result               #And we're done
        if yi >= len(ys):               #Same again, but swap roles
            result.extend(xs[xi:])
            print("*")
            return result

        #Both lists still have items, copy smaller items to result.
        if xs[xi] <= ys[yi]:
            print(xs[xi],ys[yi])
            result.append(xs[xi])
            xi += 1
            print(result, xi,yi)
        else:
            print(xs[xi],ys[yi])
            result.append(ys[yi])
            yi += 1
            print(result, xi,yi)

#print(l1)
#print(l2)
#print(merge(l1,l2))
#print("*******************************************************")
#print(l3)
#print(l4)
#rint(merge(l3,l4))
#print("*******************************************************")
print(l5)
print(l6)
print(merge(l5,l6))
