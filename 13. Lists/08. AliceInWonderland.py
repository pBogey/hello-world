"""
27.12.2018 14:28
Alice in Wonderland: how to think like a computer scientist 3rd edition
Bogdan Prădatu
"""

import time

def words_from_file(filename):
    file = open(filename,"r")
    content = file.read()
    file.close()
    flt = content.maketrans(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_‘{|}~’'\\",
        "abcdefghijklmnopqrstuvwxyz                                           ")
    word_list = content.translate(flt).split()
    return word_list

def search_linear(xs,target):
    """Find and return the index of target in sequence xs"""
    for (i,v) in enumerate(xs):
        if v == target:
            return i
    return -1

def find_unknown_words_lin(vocab,wds):
    """Return a list of words in wds that do not occur in vocab"""
    result = []
    for w in wds:
        if (search_linear(vocab,w) < 0):
            result.append(w)
    return result

def search_binary(xs,target):
    """Find and return the index of target in given sequence "lst" """
    lb = 0
    ub = len(xs)
    while True:
        if lb == ub: #empty sequence
            return -1
        
        #Place probe in the middle of the sequence
        mid_index = (lb+ub)//2

        #Fetch the item at that position
        item_at_mid = xs[mid_index]

        #print("ROI[{0}:{1}](size={2}), probed=’{3}’, target=’{4}’"
              #.format(lb, ub, ub-lb, item_at_mid, target))
        
        #How does the probed item compare to the target?
        if item_at_mid == target:
            return mid_index            #Found it
        elif item_at_mid < target:
            lb = mid_index + 1          #use upper half of sequence next time
        else:
            ub = mid_index              #use lower half of sequence next time

def find_unknown_words_bin(vocab,wds):
    """Return a list of words in wds that do not occur in vocab"""
    result = []
    for w in wds:
        if (search_binary(vocab,w) < 0):
            result.append(w)
    return result

def remove_duplicates(lst):
    """Return a list with duplicates removed from "lst" """
    lst1 = []
    for i in lst:
        if i not in lst1:
            lst1.append(i)
    return lst1

def remove_adjacent_dups(xs):
    """Return a new list in which all adjacent
        duplicates from xs have been removed."""
    result = []
    most_recent_elem = None
    for e in xs:
        if e != most_recent_elem:
            result.append(e)
            most_recent_elem = e
    return result

def find_unknowns_merge_pattern(vocab, wds):
    """ Both the vocab and wds must be sorted. Return a new
        list of words from wds that do not occur in vocab."""
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(vocab):
            result.extend(wds[yi:])
            return result
        if yi >= len(wds):
            return result

        if vocab[xi] == wds[yi]:            #Good, word exists in vocab
            yi += 1
        elif vocab[xi] < wds[yi]:           #Move past this vocab word,
            xi += 1
        else:                               #Got word that is not in vocab
            result.append(wds[yi])
            yi += 1

Alice = words_from_file("alice_in_wonderland.txt")
Vocab = words_from_file("vocab.txt")

print("********** Linear Search **********")
t0 = time.perf_counter()
missing_words = find_unknown_words_lin(Vocab,Alice)
t1 = time.perf_counter()
print("There are {0} unknown words.".format(len(missing_words)))
print("That took {0:.4f} seconds.".format(t1-t0))
print("********** Binary Search **********")
t2 = time.perf_counter()
missing_words = find_unknown_words_bin(Vocab,Alice)
t3 = time.perf_counter()
print("There are {0} unknown words.".format(len(missing_words)))
print("That took {0:.4f} seconds.".format(t3-t2))

print("\n********** Remove Duplicates **********")
print("***** Bogdan *****")
t4 = time.perf_counter()
book_words1 = remove_duplicates(Alice)
t5 = time.perf_counter()
print("There are {0} words in the book. Only {1} are unique.".
      format(len(Alice), len(book_words1)))
print("That took {0:.4f} seconds.".format(t5-t4))
print("***** HTTLACS3rd *****")
t6 = time.perf_counter()
all_book_words = words_from_file("alice_in_wonderland.txt")
all_book_words.sort()
book_words2 = remove_adjacent_dups(all_book_words)
t7 = time.perf_counter()
print("There are {0} words in the book. Only {1} are unique.".
      format(len(all_book_words), len(book_words2)))
print("That took {0:.4f} seconds.".format(t7-t6))

print("\n********** Merge Pattern **********")
t8 = time.perf_counter()
all_book_words = words_from_file("alice_in_wonderland.txt")
all_book_words.sort()
book_words = remove_adjacent_dups(all_book_words)
missing_words = find_unknowns_merge_pattern(Vocab,book_words)
t9 = time.perf_counter()
print("There are {0} unknown words.".format(len(missing_words)))
print("That took {0:.4f} seconds.".format(t9-t8))
