"""
14.12.2018 23:56
Vector Operations
Bogdan Prădatu
"""

print("Vector Operations")
print("Use the following functions:")
print("vector_mag, test_vector_mag")
print("vecto_sum, test_vector_sum")
print("vecto_scalar_mult, test_vector_scalar_mult")
print("vector_dot_prod, test_vector_dot_prod")
print("vector_cross_prod, test_vector_cross_prod\n")

v1 = [1, 2, 3]
v2 = [4, 5, 6]
s1 = 5
print("v1 =", v1, " and v2 =", v2)
print("Scalar =", s1)
v3 = [7, 8, 9]


# Vector length or magnitude
def vector_mag(vector):
    """Outputs the magnitude of a given vector"""
    sq = 0
    for i in range(len(vector)):
        sq += vector[i]**2
    result = sq**0.5
    return result


def test_vector_mag(vector1, magnitude):
    """Test for vector_mag function.
        If |Vector1| == magnitude, then test is passed"""
    if vector_mag(vector1) == magnitude:
        print("Test passed!")
    else:
        print("Test failed!")


print("\nVector Magnitude Test")
test_vector_mag([0.8, 0.6], 1)
test_vector_mag([4, 3], 5)
test_vector_mag([0], 0)
test_vector_mag([1], 1)

print("The magnitude of v1 is", vector_mag(v1))
print("The magnitude of v2 is", vector_mag(v2))
print("The magnitude of v3 is", vector_mag(v3))


# Vector Sum
def vector_sum(vector1, vector2):
    """Adds two vetors of the same length"""
    result = list(range(0, len(vector1)))
    for i in range(len(vector1)):
        result[i] = vector1[i]+vector2[i]
    return result


def test_vector_sum(vector1, vector2, vector3):
    """Test for vector_sum function.
        If Vector1 + Vector2 == Vector3, then test is passed"""
    if (vector_sum(vector1, vector2) == vector3
            and vector_sum(vector1, vector2) == vector_sum(vector2, vector1)
            and vector_sum(vector1, vector_sum(vector2, vector3)) == vector_sum(vector_sum(vector1, vector2), vector3)):
        print("Test passed!")
    else:
        print("Test failed!")


print("\nTest vector sum function")
test_vector_sum([1, 1], [1, 1], [2, 2])
test_vector_sum([1, 2], [0, 0], [1, 2])
test_vector_sum([1, 2, 1], [1, 4, 3], [2, 6, 4])
test_vector_sum([1], [4], [5])

print("v1+v2 =", vector_sum(v1, v2))


# Vector Subtraction
def vector_sub(vector1, vector2):
    """Subtracts two vetors of the same length
        Vector1 - Vector2"""
    result = list(range(0, len(vector1)))
    for i in range(len(vector1)):
        result[i] = vector1[i]-vector2[i]
    return result


def test_vector_sub(vector1, vector2, vector3):
    """Test for vector_sub function.
        If Vector1 - Vector2 == Vector3, then test is passed"""
    if vector_sub(vector1, vector2) == vector3:
        print("Test passed!")
    else:
        print("Test failed!")


print("\nTest vector sub function")
test_vector_sub([1, 1], [1, 1], [0, 0])
test_vector_sub([1, 2], [1, 4], [0, -2])
test_vector_sub([1, 2, 1], [1, 4, 3], [0, -2, -2])
test_vector_sub([1], [4], [-3])

print("v1-v2 =", vector_sub(v1, v2))


# Vector Scalar Multiple
def vector_scalar_mult(vector1, scalar1):
    """Multiplies a vector with a scalar"""
    result = list(range(0, len(vector1)))
    for i in range(len(vector1)):
        result[i] = vector1[i]*scalar1
    return result


def test_vector_scalar_mult(vector1, scalar1, vector2):
    """Test for vector_scalar_mult function.
        If Vector1 * Scalar1 == Vector2, then test is passed"""
    if (vector_scalar_mult(vector1, scalar1) == vector2
            and vector_scalar_mult(vector1, 1) == vector1
            and vector_scalar_mult(vector1, 0) == [0]*len(vector1)
            and vector_scalar_mult(vector_sum(vector1, vector2), scalar1)
            == vector_sum(vector_scalar_mult(vector1, scalar1), vector_scalar_mult(vector2, scalar1))):
        print("Test passed!")
    else:
        print("Test failed!")


print("\nTest vector scalar multiplication")
test_vector_scalar_mult([1, 2], 5, [5, 10])
test_vector_scalar_mult([1, 0, -1], 3, [3, 0, -3])
test_vector_scalar_mult([3, 0, 5, 11, 2], 7, [21, 0, 35, 77, 14])

print("v1*s1 =", vector_scalar_mult(v1, s1))
print("v2*s1 =", vector_scalar_mult(v2, s1))


# Vector Dot Product
def vector_dot_prod(vector1, vector2):
    """Outputs the dot product of two vectors of the same length"""
    result = 0
    for i in range(len(vector1)):
        result += vector1[i]*vector2[i]
    return result


def test_vector_dot_prod(vector1, vector2, scalar):
    """Test for vector_dot_prod function.
        If Vector1 * Vector2 == Scalar, then test is passed"""
    if vector_dot_prod(vector1, vector2) == scalar:
        print("Test passed!")
    else:
        print("Test failed!")


print("\nTest vector dot product")
test_vector_dot_prod([1, 1], [1, 1], 2)
test_vector_dot_prod([1, 2], [1, 4], 9)
test_vector_dot_prod([1, 2, 1], [1, 4, 3], 12)
test_vector_dot_prod([1], [2], 2)
test_vector_dot_prod([1, 0, 2], [1, 4, -5], -9)
test_vector_dot_prod([2], [3], 6)
print("v1*v2 =", vector_dot_prod(v1, v2))


def vector_cross_prod(vector1, vector2):
    """Outputs the cross product of two 3d vectors"""
    result = [vector1[1]*vector2[2]-vector1[2]*vector2[1],
              vector1[2]*vector2[0]-vector1[0]*vector2[2],
              vector1[0]*vector2[1]-vector1[1]*vector2[0]]
    return result


def test_vector_dot_prod(vector1, vector2, vector3):
    """Test for vector_cross_prod function.
        If Vector1 * Vector2 == Scalar, then test is passed"""
    if vector_cross_prod(vector1, vector2) == vector3:
        print("Test passed!")
    else:
        print("Test failed!")


print("\nTest vector_cross_prod function")
test_vector_dot_prod([0, 0, 0], [0, 0, 0], [0, 0, 0])
test_vector_dot_prod([0, 0, 0], [1, 1, 1], [0, 0, 0])
test_vector_dot_prod([-1, -1, -1], [1, 1, 1], [0, 0, 0])
test_vector_dot_prod([1, 2, 3], [3, 2, 1], [-4, 8, -4])
print("v1 x v2 is", vector_cross_prod(v1, v2))
