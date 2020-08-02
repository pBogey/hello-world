"""
Closures
23.08.2019
Bogdan Prădatu - Fluent Python
"""

# A closure is a function that retains the bindings of the free variables
# that exist when the function is defined, so that they can be used later
# when the function is invoked and the defining scope is no longer available.

# a closure is a function with an extended scope that encompasses nonglobal variables
# referenced in the body of the function but not defined there.


class Averager:
    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total/len(self.series)


def make_averager():
    series = []  # local variable because the initialization happens in the body of this function

    def averager(new_value):
        # Within averager, series is a free variable.
        # This is a technical term meaning a variable that is not bound in the local scope
        series.append(new_value)
        total = sum(series)
        return total/len(series)
    return averager


def make_averager_2():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total  # flag variables as free
        # PEP 3104 -- Access to Names in Outer Scopes
        # https://www.python.org/dev/peps/pep-3104/
        count += 1
        total += new_value
        return total/count

    return averager


if __name__ == "__main__":
    print("Class based implementation")
    avg = Averager()
    print("avg(10):", avg(10))
    print("avg(11):", avg(11))
    print("avg(12):", avg(12))
    print("\nFunction based Implementation")
    mavg = make_averager()
    print("mavg(10):", mavg(10))
    print("mavg(11):", mavg(11))
    print("mavg(12):", mavg(12))
    print("co_varnames:", mavg.__code__.co_varnames)
    print("co_freevars:", mavg.__code__.co_freevars)
    print("co_closure:", mavg.__closure__[0].cell_contents)
    # Each item in avg.__closure__ corresponds to a name in avg.__code__.co_freevars.
    # These items are cells, and they have an attribute called cell_contents wherethe actual value can be found
    print("\n")
    mavg_2 = make_averager_2()
    print("mavg_2(10):", mavg_2(10))
    print("mavg_2(11):", mavg_2(11))
    print("mavg_2(12):", mavg_2(12))
    print("co_varnames:", mavg_2.__code__.co_varnames)
    print("co_freevars:", mavg_2.__code__.co_freevars)
    print("co_closure:", mavg_2.__closure__[0].cell_contents)
    print("co_closure:", mavg_2.__closure__[1].cell_contents)
