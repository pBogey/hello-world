"""
08.01.2018
Matrix Operations - Object Oriented Programming
Bogdan Prădatu
"""

from math import cos, sin, radians

class Matrix:
    """ Define matrix of size r*c
        Use "x" to fill all entries of the matrix with given value.
        Use "u" = True to create a unity matrix of size n*n (n=r=c).
    """
    # class attributes are normally stored __dict__
    # by creating __slots__, __dict__ is no longer created
    # which should save some space. It doesn't happen in this case (why?).
    #__slots__ = ("r","c","x","u","mat")
    def __init__(self, r=0, c=None, x=None, u=False):
        """ Initialize matrix parameters
            r = number of rows
            c = number of columns
            x = fills matrix with x values
            u = unitary matrix (if set True)
        """
        self.r = r
        self.c = c
        self.x = x
        self.u = u
        self.mat = {}
        self._matrix()

    def __repr__(self):
        """ Return repr(self) """
        return f"Matrix(r={self.r},c={self.c},x={self.x},u={self.u})"

    def __str__(self):
        """ Output printed matrix """
        matrix = ""
        for i in range(self.r):
            for j in range(self.c):
                if type(self.mat.get((i,j),0)) == int:
                    matrix += f"{self.mat.get((i,j),0):>6}"
                elif type(self.mat[i,j]) == float:
                    matrix += f"{self.mat.get((i,j),0):>6.2f}"
            if j >= (self.c-1):
                matrix += "\n"
        return matrix

    def __eq__(self,other):
        """
            Comparison function.
            Returns true if is equal to other matrix
        """
        if type(self) == type(other) == Matrix:
            # Remove "0" entries from matrix
            self._clean()
            other._clean()
            if self.mat == other.mat:
                return True
        return False

    def __mul__(self, other):
        """ Returns the product of this matrix and other matrix or scalar """
        mat = Matrix(self.r, x=0)
        if type(other) == Matrix:
            mat.c = other.c
            if self.c != other.r:
                print("Incompatible matrix size. Must be m*n and n*p")
                return
            elif self.mat == {} or other.mat == {}:
                mat.mat = {}
                return mat
            else:
                for i in range(self.r):
                    for j in range(other.c):
                        mat.mat[i,j] = 0
                        for k in range(self.c):
                            mat.mat[i,j] += self.mat.get((i,k),0)*other.mat.get((k,j),0)
        elif type(other) == int:
            mat.c = self.c
            for i in range(self.r):
                for j in range(self.c):
                    mat.mat[i,j] = self.mat.get((i,j),0)*other
        else:
            del mat
            raise TypeError(f"Cannot multiply {type(self)} with {type(other)}")
        mat._clean()
        return mat

    __rmul__ = __mul__

    def __imul__(self, value):
        """ Implement self *= value """
        return self.__mul__(value)

    def __add__(self,other):
        """ Return the sum of this matrix and other matrix or integer
            If other is an int, it will be added to every element of this matrix
        """
        if type(other) == Matrix:
            if self.r == other.r and self.c == other.c:
                mat = Matrix(self.r, self.c, x=0)
                for i in range(self.r):
                    for j in range(self.c):
                        mat.mat.update({(i,j):(self.mat.get((i,j),0)+other.mat.get((i,j),0))})
        elif type(other) == int:
            mat = Matrix(self.r, self.c, x=0)
            for i in range(self.r):
                for j in range(self.c):
                    mat.mat.update({(i,j):(self.mat.get((i,j),0)+other)})
        else:
            raise TypeError(f"Cannot add {type(other)} to matrix object")
        mat._clean()
        return mat

    __radd__ = __add__

    def __iadd__(self, increment):
        """ Implement self += increment """
##        for i in range(self.r):
##            for j in range(self.c):
##                self.mat.update({(i,j):(self.mat.get((i,j),0)+increment)})
##        self._clean()
        return self.__add__(increment)

    def __sub__(self,other):
        """ Return the result of subtracting other matrix from this """
        if type(other) == Matrix:
            if self.r == other.r and self.c == other.c:
                mat = Matrix(self.r, self.c, x=0)
                for i in range(self.r):
                    for j in range(self.c):
                        mat.mat.update({(i,j):(self.mat.get((i,j),0)-other.mat.get((i,j),0))})
        elif type(other) == int:
            mat = Matrix(self.r, self.c, x=0)
            for i in range(self.r):
                for j in range(self.c):
                    mat.mat.update({(i,j):(self.mat.get((i,j),0)-other)})
        else:
            raise TypeError(f"Cannot substract {type(other)} from matrix object")
        mat._clean()
        return mat

    def __isub__(self, decrement):
        """ Implement self -= decrement """
        return self.__sub__(decrement)

    def __contains__(self,key):
        """ Return key in matrix """
        return key in self.mat.values()

    def __getitem__(self,position):
        """ matrix.__getitem__((i,j)) <==> matrix[i,j] """
        if isinstance(position, int):
            position = (position//3,position%3)
        if isinstance(position,tuple):
            if len(position)>2:
                raise IndexError("Too many indices for matrix")
            elif (0 > position[0] or position[0] >= self.r or
                  0 > position[1] or position[1] >= self.c):
                raise IndexError("Matrix index out of range")
            return self.mat.get(position,0)

    def __setitem__(self, position, value):
        """ set self[position] to value, where position is of form (i,j) """
        if isinstance(position, int):
            position = (position//3,position%3)
        if isinstance(position,tuple):
            if len(position)>2:
                raise IndexError("Too many indices for matrix")
            elif (0 > position[0] or position[0] >= self.r or
                  0 > position[1] or position[1] >= self.c):
                raise IndexError("Matrix index out of range")
        self.mat.update({position:value})
        self._clean()
        return self

    def _matrix(self):
        """ Create matrix.
            If "x" or "u" are not given, then a random r*x matrix is created
        """
        from random import randrange
        if self.c == None:
            self.c = self.r
        if self.u == False:
            if self.x == None:
                for i in range(self.r):
                    for j in range(self.c):
                        e = randrange(10)
                        if e != 0:
                            self.mat[i,j] = e
            elif self.x == 0:
                self.mat = {}
            else:
                for i in range(self.r):
                    for j in range(self.c):
                        self.mat[i,j] = self.x
        elif self.u == True and self.r == self.c:
            e = 0
            for i in range(self.r):
                self.mat[i,i] = 1
        elif self.u == True and self.r != self.c:
            print("Identity matrix must be of size n*n. 'r' must equal 'c'")
            del self.mat, self.u, self.c, self.x, self.r
            return

    def transpose(self):
        """ Return the transpose of this matrix """
        mat = Matrix(self.c,self.r,0)
        if self.mat == {}:
            mat.mat = self.mat
            return mat
        else:
            for i in range(self.c):
                for j in range(self.r):
                    mat.mat[i,j] = self.mat.get((j,i),0)
        return mat

    def rotate(self, d=2, z=0, y=0, x=0):
        """ Create rotation matrix (positive angle values: counterclockwise).
            d = 2 for 2D or 3 for 3D rotation matrix
            z - angle of rotation about Z axis
            y - angle of rotation about Y axis
            x - angle of rotation about Z axis
        """
        a = radians(x)
        b = radians(y)
        c = radians(z)
        if d == 2:
            mat = Matrix(2, x=0)
            mat.mat = {(0,0):round(cos(c),5),(0,1):-round(sin(c),5),
                   (1,0):round(sin(c),5),(1,1):round(cos(c),5)}
        if d == 3:
            mat = Matrix(3, x=0)
            mat.mat = {(0,0):(round(cos(b),5)*round(cos(c),5)),
                    (0,1):(-round(cos(b),5)*round(sin(c),5)),
                    (0,2):round(sin(b),5),
                   (1,0):(round(cos(a),5)*round(sin(c),5)
                    +round(sin(a),5)*round(sin(b),5)*round(cos(c),5)),
                    (1,1):(round(cos(a),5)*round(cos(c),5)
                    -round(sin(a),5)*round(sin(b),5)*round(sin(c),5)),
                    (1,2):(-round(sin(a),5)*round(cos(b),5)),
                   (2,0):(round(sin(a),5)*round(sin(c),5)
                    -round(cos(a),5)*round(sin(b),5)*round(cos(c),5)),
                    (2,1):(round(sin(a),5)*round(cos(c),5)
                    +round(cos(a),5)*round(sin(b),5)*round(sin(c),5)),
                    (2,2):(round(cos(a),5)*round(cos(b),5))}
        return mat*self

    def determinant(self):
        """ Return the determinat of this square matrix """
        self.det = 0
        if self.mat == {}:
            self.det = 1
            return self.det
        elif self.r != self.c:
            print("Determinants can only be computed for n*n matrices """)
            return
        elif self.r == self.c == 1:
            self.det = self.mat[0,0]
            return self.det
        elif self.r == self.c == 2:
            self.det = (self.mat.get((0,0),0)*self.mat.get((1,1),0) -
                        self.mat.get((0,1),0)*self.mat.get((1,0),0))
            return self.det
        else:
            mat = Matrix(self.r-1)
            for k in range(self.r):
                x = 0
                y = 0
                for i in range(1,self.r):
                    for j in range(self.r):
                        if j == k:
                            continue
                        else:
                            mat.mat[x,y] = self.mat.get((i,j),0)
                            y += 1
                            if y == self.r-1:
                                x += 1
                                y = 0
                mat.determinant()
                self.det = self.det + self.mat.get((0,k),0) * ((-1)**k) * mat.det
        return self.det

    def submatrix(self,i=[],j=[]):
        """ Return a submatrix of this matrix, by eliminating rows 'i' and columns 'j',
            where 'i' and 'j' can be integers, lists or tuples.
        """
        mat = Matrix(self.r, self.c, x=0)
        case = 0
        if ((type(i) == list or type(i) == tuple) and
            (type(j) == list or type(j) == tuple)):
            case = 1
            r_cor = 0
            c_cor = 0
            for e in i:
                if e <= 0:
                    r_cor += 1
            for e in j:
                if e <= 0:
                    c_cor += 1
            mat.r = self.r - len(i) + r_cor
            mat.c = self.c - len(j) + c_cor
        elif type(i) == type(j) == int:
            case = 2
            if i <= 0 and j <= 0:
                return self
            if i >= 1:
                mat.r = self.r - 1
            else:
                mat.r = self.r
            if j >= 1:
                mat.c = self.c - 1
            else:
                mat.c = self.c
        elif (type(i) == list or tuple) and type(j) == int:
            case = 3
            r_cor = 0
            for e in i:
                if e <= 0:
                    r_cor += 1
            mat.r = self.r - len(i) + r_cor
            mat.c = self.c - 1
        elif type(i) == int and (type(j) == list or tuple):
            case = 4
            c_cor = 0
            for e in j:
                if e <= 0:
                    c_cor += 1
            mat.r = self.r - 1
            mat.c = self.c - len(j) + c_cor
        else:
            print("Arguments must be of type list, tuple or integer")
            del mat
            return
        x = 0
        y = 0
        for r in range(self.r):
            for c in range(self.c):
                if case == 1:
                    if r+1 in i or c+1 in j:
                        continue
                elif case == 2:
                    if r+1 == i or c+1 == j:
                        continue
                elif case == 3:
                    if r+1 in i or c+1 == j:
                        continue
                elif case == 4:
                    if r+1 == i or c+1 in j:
                        continue
                mat.mat[x,y] = self.mat.get((r,c),0)
                y += 1
                if y >= mat.c:
                    y = 0
                    x += 1
        mat._clean()
        return mat

    def sum_row(self, r1, r2):
        """ Return the result of adding row 'r1' to row 'r2' """
        mat = Matrix(self.r, self.c, x=0)
        mat.mat = self.mat.copy()
        for i in range(self.c):
            mat.mat[r2-1,i] = self.mat.get((r1-1,i),0)+self.mat.get((r2-1,i),0)
        mat._clean()
        return mat

    def sum_col(self, c1, c2):
        """ Return the result of adding column 'c1' to row 'c2' """
        mat = Matrix(self.r, self.c, x=0)
        mat.mat = self.mat.copy()
        for i in range(self.r):
            mat.mat[i,c2-1] = self.mat.get((i,c1-1),0)+self.mat.get((i,c2-1),0)
        mat._clean()
        return mat

    def _clean(self):
        """ Remove 0 entries from this matrix's data structure """
        if 0 in self.mat.values():
            for i in range(self.r):
                for j in range(self.c):
                    if (i,j) in self.mat and self.mat[i,j] == 0:
                        self.mat.pop((i,j))

    def _fill(self):
        """ Update this matrix with all 0 entries """
        for i in range(self.r):
            for j in range(self.c):
                if (i,j) not in self.mat:
                    self.mat[i,j] = 0
                    
    def insert(self, i, j, v):
        """ Insert value 'v' at row 'i' and column 'j'.
            Note: The first element is at (i=0, j=0)
        """
        self.mat.update({(i,j):v})
        self._clean()
        if i > self.r-1:
            self.r = i+1
        if j > self.c-1:
            self.c = j+1
        return
if __name__ == "__main__":
    help(Matrix)
    
    m1 = Matrix(3)
    m2 = Matrix(3)

    print("m1:")
    print(m1)
    print("m2:")
    print(m2)
