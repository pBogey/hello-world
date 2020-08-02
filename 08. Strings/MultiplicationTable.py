"""
Multiplication table
02.11.2018 22:36
Bogdan Prădatu
"""


def multiples(n, x):
    for i in range(1, x+1):
        print("{:>4}".format(n*i), end=" ")
    return print()


def mult_table():
    while True:
        try:
            n = int(input("Please insert the desired size of the table:"))
        except ValueError:
            print("Please only input integers")
            continue
        else:
            n = 0
            break

    for i in range(1, n+1):
        multiples(i, n)


mult_table()
