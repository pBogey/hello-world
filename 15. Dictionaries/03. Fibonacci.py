"""
05.01.2019 00:25
Fibonacci
Bogdan Prădatu - from how to think like a computer scientist 1st edition
"""

previous = {0: 1, 1: 1}


def fibonacci(n):
    if n in previous:
        return previous[n]
    else:
        new_value = fibonacci(n-1) + fibonacci(n-2)
        previous[n] = new_value
        return new_value


print(fibonacci(200))
