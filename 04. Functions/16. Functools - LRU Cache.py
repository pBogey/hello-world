"""
Functools - LRU Cache
23.08.2019
Bogdan Prădatu - Fluent Python
"""

# lru_cache = Least Recently Used
# used for memoization -> saving the results of previous invocations
# of an expensive function, avoiding repeat computations on previously
# used arguments.

from Decorators_ClockDeco import clock2
import functools


@clock2
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)


@functools.lru_cache()  # must be invoked as a regular function, with "()"
@clock2
def fibonacci2(n):
    if n < 2:
        return n
    return fibonacci2(n-2) + fibonacci2(n-1)


if __name__ == "__main__":
    print("Without LRU Cache:")
    print(fibonacci(6))
    print("\nWith LRU Cache")
    print(fibonacci2(6))
