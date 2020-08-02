"""
29.12.2018 15:34
Matrix Operations
Bogdan Prădatu
"""


def matrix(r, c=None, x=None, u=False):
    """ Create random matrix of size r*c
        Use "x" to fill all entries of the matrix with given value.
        Use "u" = True to create a unity matrix of size n*n (r=c=n)."""
    from random import randrange
    mat = []
    if c is None:
        c = r
    # print("Matrix:")
    if u is False:
        for i in range(r):
            mat.append([])
            if x is None:
                for j in range(c):
                    e = randrange(10)
                    mat[i].append(e)
            else:
                for j in range(c):
                    mat[i].append(x)
           # print(mat[i])
    elif u is True and r == c:
        e = 0
        for i in range(r):
            mat.append([])
            for j in range(c):
                mat[i].append(e)
            mat[i][i] = 1
    elif u is True and r != c:
        return "Identity matrix must be of size n*n. 'r' must equal 'c'"
    return mat


def matrix_sum(m1, m2):
    """Addition of two r*c matrices"""
    if not m1:
        mat = []
        return mat
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        return "Only matrices of the same size can be summed"
    else:
        mat = matrix(len(m1), len(m1[0]), 0)
        # print(mat)
        for i in range(len(m1)):
            for j in range(len(m1[i])):
                mat[i][j] = (m1[i][j] + m2[i][j])
                # print(mat[i][j])
    return mat


def matrix_sub(m1, m2):
    """Subtraction of two r*c matrices"""
    if not m1:
        mat = []
        return mat
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        return "Only matrices of the same size can be subtracted"
    else:
        mat = matrix(len(m1), len(m1[0]), 0)
        # print(mat)
        for i in range(len(m1)):
            for j in range(len(m1[i])):
                mat[i][j] = (m1[i][j] - m2[i][j])
                # print(mat[i][j])
    return mat


def matrix_scalar_prod(m, s):
    """Scalar product of matrix "m" by scalar "s" """
    if not m:
        mat = []
        return mat
    else:
        mat = matrix(len(m), len(m[0]), 1)
        for i in range(len(m)):
            for j in range(len(m[i])):
                mat[i][j] = s*m[i][j]
                # print(mat[i][j])
    return mat


def matrix_prod(m1, m2):
    """Returns the product of two matrices
        m1 of size m*n and m2 of size n*r"""
    if not m1:
        mat = []
        return mat
    elif len(m1[0]) != len(m2):
        return "Incompatible matrix size. Must be n*m and m*p"
    else:
        mat = matrix(len(m1), len(m2[0]), 0)
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                for k in range(len(m1[0])):
                    mat[i][j] += m1[i][k]*m2[k][j]
    return mat


def matrix_transpose(m):
    """Return the transpose of matrix "m" """
    if not m:
        mat = []
        return mat
    else:
        mat = matrix(len(m), len(m[0]), 0)
        # print(mat)
        for i in range(len(m)):
            for j in range(len(m[i])):
                mat[i][j] = m[j][i]
                # print(mat[i][j])
    return mat


def rot_mat(m, z=0, y=0, x=0):
    """ Create rotation matrix (positive angle values: counterclockwise)
        m = 2 for 2D or 3 for 3D rotation matrix (only z angle needed)
        z - rotation about Z axis
        y - rotation about Y axis
        x - rotation about X axis"""
    from math import cos, sin, radians
    a = radians(x)
    b = radians(y)
    c = radians(z)
    if m == 2:
        mat = [[round(cos(c), 5), -round(sin(c), 5)],
               [round(sin(c), 5), round(cos(c), 5)]]
    elif m == 3:
        mat = [[round(cos(b), 5)*round(cos(c), 5),
                -round(cos(b), 5)*round(sin(c), 5),
                round(sin(b), 5)],
               [round(cos(a), 5)*round(sin(c), 5)
                + round(sin(a), 5)*round(sin(b), 5)*round(cos(c), 5),
                round(cos(a), 5)*round(cos(c), 5)
                - round(sin(a), 5)*round(sin(b), 5)*round(sin(c), 5),
                - round(sin(a), 5)*round(cos(b), 5)],
               [round(sin(a), 5)*round(sin(c), 5)
                - round(cos(a), 5)*round(sin(b), 5)*round(cos(c), 5),
                round(sin(a), 5)*round(cos(c), 5)
                + round(cos(a), 5)*round(sin(b), 5)*round(sin(c), 5),
                round(cos(a), 5)*round(cos(b), 5)]]
    else:
        raise Exception("Only 2D or 3D matrix are supported.")
    return mat


def mat_det(m):
    """Returns the determinant of a n*n square matrix"""
    det = 0
    if len(m) == 0:
        det = 1
        return det
    elif len(m) == 1:
        det = m[0]
        return det
    if len(m) != len(m[0]):
        return "Determinants can only be computed for n*n matrices"
    n = len(m)
    if n == 2:
        det = m[0][0]*m[1][1]-m[1][0]*m[0][1]
    else:
        M = matrix((n-1), (n-1))
        for k in range(n):
            x = 0
            y = 0
            for i in range(1, n):
                for j in range(n):
                    if j == k:
                        continue
                    else:
                        M[x][y] = m[i][j]
                        y += 1
                        if y == n-1:
                            x += 1
                            y = 0
            # draw_matrix(M)
            det = det + m[0][k] * ((-1)**k) * mat_det(M)
    return det


def draw_matrix(m):
    for i in range(len(m)):
        print(m[i])


print("***** Test *****")
mat0 = [[1, 2, 1, 0], [0, 3, 1, 1], [-1, 0, 3, 1], [3, 1, 2, 0]]
mat1 = matrix(3, 3)
mat2 = matrix(3, 3)
mat3 = matrix(3, 3)
print("Matrix 0:")
draw_matrix(mat0)
print("Matrix 1:")
draw_matrix(mat1)
print("Matrix 2:")
draw_matrix(mat2)
print("Matrix 3:")
draw_matrix(mat3)

print("\n*** Sum ***")
print("Matrix 1 + Matrix 2")
ms = matrix_sum(mat1, mat2)
draw_matrix(ms)
print("\nA+B = B+A:", matrix_sum(mat1, mat2) == matrix_sum(mat2, mat1))
print("(A+B)+C = A+(B+C):", matrix_sum(matrix_sum(mat1, mat2), mat3)
      == matrix_sum(mat1, matrix_sum(mat2, mat3)))
print("A+O = A:", matrix_sum(mat1, matrix(3, 3, 0)) == mat1)
print("\n*** Subtraction ***")
print("Matrix 1 - Matrix 2")
msb = matrix_sub(mat1, mat2)
draw_matrix(msb)
print("\nA+(-A)=O:", matrix_sum(mat1, matrix_sub(matrix(3, 3, 0), mat1))
      == matrix(3, 3, 0))
print("\n*** Scalar Product ***")
print("Matrix 1 * 2")
msp = matrix_scalar_prod(mat1, 2)
draw_matrix(msp)
print("\nc(A+B) = cA+cB:", matrix_scalar_prod(matrix_sum(mat1, mat2), 2)
      == matrix_sum(matrix_scalar_prod(mat1, 2), matrix_scalar_prod(mat2, 2)))
print("(c+d)A = cA + dA:", matrix_scalar_prod(mat2, (2+3)) ==
      matrix_sum(matrix_scalar_prod(mat2, 2), matrix_scalar_prod(mat2, 3)))
print("c(dA) = cd(A):", matrix_scalar_prod(matrix_scalar_prod(mat3, 2), 3)
      == matrix_scalar_prod(mat3, (3*2)))
print("1*A=A:", matrix_scalar_prod(mat1, 1) == mat1)
print("\n*** Matrix Product ***")
print("Matrix 1 * Matrix 2")
mp = matrix_prod(mat1, mat2)
draw_matrix(mp)
print("\n(AB)C = A(BC):", matrix_prod(matrix_prod(mat1, mat2), mat3)
      == matrix_prod(mat1, matrix_prod(mat2, mat3)))
print("A(B+C) = AB + AC:", matrix_prod(mat1, matrix_sum(mat2, mat3))
      == matrix_sum(matrix_prod(mat1, mat2), matrix_prod(mat1, mat3)))
print("(A+B)C = AC + BC:", matrix_prod(matrix_sum(mat1, mat2), mat3)
      == matrix_sum(matrix_prod(mat1, mat3), matrix_prod(mat2, mat3)))
print("k(AB) = (kA)B = A(kB):", matrix_scalar_prod(matrix_prod(mat1, mat2), 2)
      == matrix_prod(matrix_scalar_prod(mat1, 2), mat2) 
      == matrix_prod(mat1, matrix_scalar_prod(mat2, 2)))
print("I*A = A = A*I:", matrix_prod(matrix(3, 3, u=True), mat1) == mat1
      == matrix_prod(mat1, matrix(3, 3, u=True)))

print("\n*** Transpose ***")
print("Matrix 1 Transposed")
mt = matrix_transpose(mat1)
draw_matrix(mt)
print("(At)t = A:", matrix_transpose(matrix_transpose(mat1)) == mat1)
print("(A+B)t = At+Bt:", matrix_transpose(matrix_sum(mat1, mat2))
      == matrix_sum(matrix_transpose(mat1), matrix_transpose(mat2)))
print("(kA)t = k(A)t:", matrix_transpose(matrix_scalar_prod(mat1, 2))
      == matrix_scalar_prod(matrix_transpose(mat1), 2))
print("(AB)t = BtAt:", matrix_transpose(matrix_prod(mat1, mat2))
      == matrix_prod(matrix_transpose(mat2), matrix_transpose(mat1)))
print("\n*** Rotation Matrix ***")
print("2D 90 degrees rotation:")
draw_matrix(rot_mat(2, 90))
print("3D 90 degrees rotation about X axis:")
draw_matrix(rot_mat(3, 0, 0, 90))
print("No rotation:")
draw_matrix(rot_mat(3, 0, 0, 0))
print("Rotate Matrix 1 with 90 degrees about the Z axis:")
draw_matrix(matrix_prod(rot_mat(3, 90), mat1))
print("\n*** Matrix Determinant ***")
print("Δmat0:", mat_det(mat0))
print("Δmat1:", mat_det(mat1))
print("Δmat2:", mat_det(mat2))
print("Δmat3:", mat_det(mat3))
