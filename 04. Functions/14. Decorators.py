"""
Decorators
23.08.2019
Bogdan Prădatu - Fluent Python
"""

# A decorator is a callable that takes another function as argument.
# Decorators replace the decorated function with a different one.
# !! Decorators are executed after the decorator function is defined: at import time (when a module is loaded.) !!
# !! Decorated functions only run when they are invoked. !!

registry = []


def register(func):
    print(f'running register {func}')
    registry.append(func)
    return func


@register
def f1():
    print('running f1()')


@register
def f2():
    print('running f2()')


def f3():
    print('running f3()')


def main():
    print("\nRegister runs (twice) before any other function in the module.\n"
          "When register is called, it receives as an argument the function object being decorated\n")
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()


from Decorators_ClockDeco import clock, clock2
import time


@clock
def snooze(seconds):
    time.sleep(seconds)


@clock
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)


@clock2
def factorial2(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact


if __name__ == "__main__":
    main()

    print("\n")
    print('*' * 20, 'Calling snooze(.123)')
    snooze(.123)
    print('*' * 20, 'Calling factorial(6)')
    print('6! =', factorial(6))
    print('*' * 20, 'Calling factorial2(6)')
    print('6! =', factorial2(6))
    # factorial holds a reference to clocked
    # each time factorial(n) is called, clocked(n) gets executed
    print("factorial.__name__:", factorial.__name__)
    # functools.wraps copies the relevant attirbutes from func to clocked
    print("factorial2.__name__:", factorial2.__name__)
