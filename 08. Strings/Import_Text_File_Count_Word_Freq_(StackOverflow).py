from turtle import Screen, Turtle
from collections import defaultdict

PUNCTUATION = "~`!@#$%^&*()_-=+[{]}\\|'\";:,<.>/?"

def remove_punctuation(text):
    """ Removes punctuation characters from given text """

    text_wo_punctuation = ""

    for letter in text:
        if letter not in PUNCTUATION:
            text_wo_punctuation += letter

    return text_wo_punctuation

def count_words(filename):
    """ Returns a dictionary of words and word count from "file" """

    dictionary = defaultdict(int)  # if you won't use Counter, at least use defaultdict()

    with open(filename) as file:
        text = remove_punctuation(file.read()).lower().split()

        for word in text:
            dictionary[word] += 1

    return dictionary

def dict_sort(d, reverse=False):
    """
    Sort given dictionary "d" values (& keys) in ascending (default)
    or descending (reverse = True) order
    Outputs tuple of: list of keys, list of values
    Recommended format for output: k, v = dict_sort(d)
    """

    key_list = list(d.keys())
    value_list = list(d.values())

    for _ in range(len(value_list) - 1):
        for i in range(len(value_list) - 1):
            if reverse:
                if value_list[i] > value_list[i+1]:
                    value_list[i], value_list[i+1] = value_list[i+1], value_list[i]
                    key_list[i], key_list[i+1] = key_list[i+1], key_list[i]
            else:
                if value_list[i] < value_list[i+1]:
                    value_list[i], value_list[i+1] = value_list[i+1], value_list[i]
                    key_list[i], key_list[i+1] = key_list[i+1], key_list[i]

    return key_list, value_list

def word_freq():
    """ Input how many words to plot on graph """

    while True:
        try:
            n_freq = int(input("How many of the most frequent words would you like to display?\n"))

            if not 1 <= n_freq <= 10:
                print("Please input an integer between 1 and 10:")
                continue

        except ValueError:
            print("Please input an integer between 1 and 10:")
            continue
        else:
            break

    return n_freq

def graph_word_freq(n, f, w):
    """
    Draw bar chart of most frequent words in text
    n: number of words to plot (between 1 and 10)
    f: word frequency list
    w: word list
    """

    window = Screen()
    window.bgcolor("honeydew")
    window.title("Most Frequent Words")

    if f[0] < 960:
        width = 60
        spacing = 20
        y = 500
        y_pos = -480
        x_pos = - (30 + 40 * (n - 1))
    else:
        width = 100
        spacing = 40
        y = f[0] / 2 + 20
        y_pos = -f[0] / 2
        x_pos = - (50 + 70 * (n - 1))

    window.setworldcoordinates(-y, -y, y, y)
    tortoise = Turtle(visible=False)
    tortoise.speed('fastest')  # because I have no patience

    tortoise.penup()
    tortoise.setposition(x_pos, y_pos)

    for i in range(n):
        if f[i] < (f[0] - f[n]) / 3:
            tortoise.color("SeaGreen", "ForestGreen")
        elif (f[0] - f[n]) / 3 <= f[i] < (f[0] - f[n]) / 1.5:
            tortoise.color("orange", "gold")
        else:
            tortoise.color("coral3", "IndianRed")

        tortoise.left(90)

        tortoise.begin_fill()

        tortoise.forward(f[i])
        tortoise.right(90)

        tortoise.forward(1/2 * width)
        tortoise.write(f[i], align='center')
        tortoise.forward(1/2 * width)

        tortoise.right(90)
        tortoise.forward(f[i])

        tortoise.end_fill()

        tortoise.forward(20)
        tortoise.right(90)

        tortoise.forward(1/2 * width)
        tortoise.write(w[i], align='center')
        tortoise.backward(1/2 * width)

        tortoise.right(90)
        tortoise.forward(20)
        tortoise.right(90)
        tortoise.forward(spacing)

    window.exitonclick()

dictionary = count_words("New Text Document (2).txt")

words, values = dict_sort(dictionary, reverse=False)

n_freq = word_freq()

graph_word_freq(n_freq, values, words)
