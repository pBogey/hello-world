"""
28.12.2018 17:07
Eight Queens Puzzle - https://en.wikipedia.org/wiki/Eight_queens_puzzle
Bogdan Prădatu - from how to think like a computer scientist 3rd edition
"""
import time
import pygame
print("This program will output solutions for the Eight Queen Puzzle:\n\n")

def share_diagonal(x0,y0,x1,y1):
    """Is (x0,y0) on a shared diagonal with (x1,y1)?"""
    dy = abs(y1 - y0)       #Calc the absolute y distance
    dx = abs(x1 - x0)       #Calc the absolute x distance
    return dx == dy         #They clash if dx == dy

def col_clashes(bs,c):
    """ Return True if the queen at column c clashes
        with any queen to its left
    """

    for i in range(c):                  #Look at all columns to the left of c
        if share_diagonal(i,bs[i],c,bs[c]):
            return True
    return False                        #No clahses - col c has a safe placement

def has_clashes(the_board):
    """ Detrermine whether we have any queens clashing on the diagonals.
        We're assuming here that the_board is a permutation of column
        numbers, so we're not explicitly checking row or column clashes.
    """

    for col in range(1,len(the_board)):
        if col_clashes(the_board,col):
            return True
    return False

def main():
    import random
    import draw_queens
    rng = random.Random()           #Instantiate a generator
    bd = list(range(8))             #Generate the initial permutation
    num_found = 0
    tries = 0
    while num_found < 10:
        rng.shuffle(bd)
        tries += 1
        if not has_clashes(bd):
            print("Found solution {0} in {1} tries.".format(bd,tries))
            draw_quens.draw_board(bd)
            tries = 0
            num_found += 1
            
t0 = time.perf_counter()
main()
t1 = time.perf_counter()
print(t1-t0)

