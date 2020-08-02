"""
27.12.2018 12:10
Merge Sorted Lists: from how to think like a computer scientist 3rd edition
Bogdan Prădatu
"""

l1 = []
l2 = []
l3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l4 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
l5 = [0, 2, 4, 6, 8]
l6 = [1, 3, 5, 7, 9]
l7 = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]


def merge(xs, ys):
    """Merge sorted lists xs and ys. Return a sorted result"""
    result = []
    xi = 0
    yi = 0
    # print("Len xs:",len(xs),"\nLen ys:",len(ys))
    while True:
        if xi >= len(xs):               # If xs list is finished
            result.extend(ys[yi:])      # Add remaining items from ys
            # print("*")
            return result               # And we're done
        if yi >= len(ys):               # Same again, but swap roles
            result.extend(xs[xi:])
            # print("*")
            return result

        # Both lists still have items, copy smaller items to result.
        if xs[xi] <= ys[yi]:
            # print(xs[xi],ys[yi])
            result.append(xs[xi])
            xi += 1
            # print(result, xi,yi)
        else:
            # print(xs[xi],ys[yi])
            result.append(ys[yi])
            yi += 1
            # print(result, xi,yi)


def merge_common(xs, ys):
    """Merge sorted lists xs and ys. Return only elements common to both lists"""
    result = []
    xi = 0
    yi = 0
    while True:
        if xi >= len(xs):               # If xs list is finished
            return result               # And we're done
        if yi >= len(ys):               # Same again, but swap roles
            return result
        if xs[xi] < ys[yi]:
            xi += 1
        elif xs[xi] > ys[yi]:
            yi += 1
        else:
            result.append(xs[xi])
            yi += 1
            xi += 1


def merge_exclude(xs, ys, reverse=False):
    """
        Merge sorted lists xs and ys. Return a new list containing
        only elements found in xs (reverse = False) or ys (reverse = True)
    """
    result = []
    xi = 0
    yi = 0
    if reverse is False:
        while True:        
            if xi >= len(xs):               # If xs list is finished
                return result               # And we're done
            if yi >= len(ys):               # Same again, but swap roles
                result.extend(xs[xi:])
                return result
            if xs[xi] == ys[yi]:
                xi += 1
            elif xs[xi] > ys[yi]:
                yi += 1
            else:
                result.append(xs[xi])
                xi += 1                
    if reverse is True:
        while True:        
            if xi >= len(xs):               # If xs list is finished
                result.extend(ys[yi:])      # Add remaining items from ys
                return result               # And we're done
            if yi >= len(ys):               # Same again, but swap roles
                return result
            if xs[xi] == ys[yi]:
                yi += 1
            elif xs[xi] < ys[yi]:
                xi += 1
            else:
                result.append(ys[yi])
                yi += 1


def merge_bagdiff(xs, ys):
    """Bagdiff"""
    result = []
    xi = 0
    yi = 0
    while True:
        if xi >= len(xs):               # If xs list is finished
            result.extend(ys[yi:])      # Add remaining items from ys
            return result               # And we're done
        if yi >= len(ys):               # Same again, but swap roles
            result.extend(xs[xi:])
            return result
        if xs[xi] < ys[yi]:
            result.append(xs[xi])
            xi += 1
        elif xs[xi] > ys[yi]:
            yi += 1
        else:
            xi += 1
            yi += 1


print("l1:", l1)
print("l2:", l2)
print("l3:", l3)
print("l4:", l4)
print("l5:", l5)
print("l6:", l6)
print("l7:", l7)

print("\n***** Merge *****")
print("merge(l1,l2):", merge(l1, l2))
print("merge(l1,l3):", merge(l1, l3))
print("merge(l3,l4):", merge(l3, l4))
print("merge(l5,l6):", merge(l5, l6))
print("\n***** Merge Common *****")
print("merge_common(l1,l2):", merge_common(l1, l2))
print("merge_common(l1,l3):", merge_common(l1, l2))
print("merge_common(l3,l7):", merge_common(l3, l7))
print("merge_common(l3,l5):", merge_common(l3, l5))
print("merge_common(l3,l6):", merge_common(l3, l6))
print("\n***** Merge Exclude *****")
print("merge_exclude(l1,l2):", merge_exclude(l1, l2))
print("merge_exclude(l1,l3):", merge_exclude(l1, l3))
print("merge_exclude(l3,l5):", merge_exclude(l3, l5))
print("merge_exclude(l3,l6):", merge_exclude(l3, l6))
print("merge_exclude(l4,l7):", merge_exclude(l4, l7))

print("\n***** Bagdiff *****")
print("merge_bagdiff(l1,l2):", merge_bagdiff(l1, l2))
print("merge_bagdiff(l1,l3):", merge_bagdiff(l1, l3))
print("merge_bagdiff(l3,l5):", merge_bagdiff(l3, l5))
print("merge_bagdiff(l3,l6):", merge_bagdiff(l3, l6))
print("merge_bagdiff(l7,l3):", merge_bagdiff(l7, l3))
