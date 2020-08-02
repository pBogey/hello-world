"""
30.08.2018 20:19
Taken from How To Think Like a Computer Scientist 3rd edition
Collatz 3n+1 sequence: the interesting question was first posed by a German mathematician called Lothar Collatz: the
Collatz conjecture (also known as the 3n + 1 conjecture), is that this sequence terminates for all positive values of n.
So far, no one has been able to prove it or disprove it! (A conjecture is a statement that might be true, but nobody
knows for sure.)
"""


def arguments(prompt_msg):
    while True:  # create loop for error check
        try:
            variable = float(input(prompt_msg))  # convert user input to integer
        except ValueError:
            # if input is not a number, retry
            print("invalid number, please try again:")
            continue
        else:
            # user input was valid, end
            break
    return variable


n = arguments("Please input a value for n: ")


print("n =", n, "\n")
print('while n != 1: \nprint(n, end="; ") \nif n % 2 == 0: \nn = n // 2 \nelse: \nn = n * 3 + 1\n\n')


while n != 1:
    print(n, end="; " '\t')  # put ";" after every "n" printed and shift cursor to next tab stop
    if n % 2 == 0:           # n is even
        n = n // 2
    else:                    # n is odd
        n = n * 3 + 1
print(n, end=".\n")          # print "." after the last "n" printed
