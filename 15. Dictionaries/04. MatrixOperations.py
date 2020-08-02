"""
05.01.2019 00:39
Matrix Operations
Bogdan Prădatu
"""


def matrix(r, c=None, x=None, u=False):
    """ Create random matrix of size r*c
        Use "x" to fill all entries of the matrix with given value.
        Use "u" = True to create a unity matrix of size n*n (r=c=n)."""
    from random import randrange
    mat = {}
    if c is None:
        c = r
    # print("Matrix:")
    if u is False:
        for i in range(r):
            if x is None:
                for j in range(c):
                    e = randrange(10)
                    if e != 0:
                        mat[i, j] = e
            else:
                for j in range(c):
                    mat[i, j] = x
            # print(mat[i])
    elif u is True and r == c:
        e = 0
        for i in range(r):
            for j in range(c):
                mat[i, j] = e
            mat[i, i] = 1
    elif u is True and r != c:
        return "Identity matrix must be of size n*n. 'r' must equal 'c'"
    return mat


def draw_matrix(m):
    k = m.keys()
    for i in range(max(k)[0]):
        for j in range(max(k)[1]):
            print(m[i, j])


matx = matrix(3)
draw_matrix(matx)
