"""
15.10.2018 22:27
Newton's method for square roots

from how to think like a computer scientist v3
"""

print("This program approximates the square root of a given number")
print("Use sqrt(x) to find the square root of x")


def sqrt(n):
    approx = n/2
    while True:
        better = (approx + n/approx)/2
        if abs(approx - better) < 0.0001:
            return better
        approx = better
