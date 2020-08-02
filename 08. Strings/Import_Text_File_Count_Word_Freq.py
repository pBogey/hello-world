"""
Strings: plot on a bar chart the "n" most frequent of a given text
29.10.2018 19:32
Bogdan Prădatu
"""


def remove_punctuation(text):
    """"Removes punctuation characters from given text"""
    punctuation = "~`!@#$%^&*()_-=+[{]}\\|'\";:,<.>/?"
    text_wo_punctuation = ""
    for word in text:
        if word not in punctuation:
            text_wo_punctuation += word
    return text_wo_punctuation


with open(r'Gasoline Engines.txt') as f:
    text = f.read().lower()
    t = remove_punctuation(text).split()
    dictionary = {}
    for word in t:
        if word in dictionary:
            dictionary[word] = dictionary[word] + 1
        else:
            dictionary[word] = 1


def word_freq():
    while True:
        try:
            n_freq = int(input("How many of the most frequent words would you like to display?\n"))
            if n_freq < 1 or n_freq > 10:
                print("Please input an integer between 1 and 10:")
                continue
        except ValueError:
            print("Please input an integer between 1 and 10:")
            continue
        else:
            break
    return n_freq


def graph_word_freq(n, f, w):                     # create function to draw chart
    """Draw bar chart of most frequent words in text
        n: number of words to plot (between 1 and 10)
        f: word frequency list
        w: word list"""

    import turtle                                       # import turtle module
    window = turtle.Screen()                            # create screen
    window.bgcolor("honeydew")                          # define screen color
    window.title("Most Frequent Words")                 # set window title
    if f[0] < 960:
        y = 500
        y_pos = -480
        width = 60
        spacing = 20
        x_pos = -(30+40*(n-1))
    else:
        width = 100
        spacing = 40
        y = f[0]/2+20
        y_pos = -f[0]/2
        x_pos = -(50+70*(n-1))
   
    # turtle.screensize(y,y)                              # set window size
    turtle.setworldcoordinates(-y, -y, y, y)
    tortoise = turtle.Turtle()                          # create turtle
    tortoise.hideturtle()                               # hide turtle stamp
    tortoise.penup()                                    # raise turtle pen
    tortoise.setposition(x_pos, y_pos)                   # position turtle
    tortoise.pendown()                                  # put turtle pen down
    tortoise.speed(5)                                   # set drawing speed

    for i in range(n):
        if abs(f[i]) < ((f[0]-f[n])/3):
            tortoise.color("SeaGreen", "ForestGreen")    # set turtle color
        elif ((f[0]-f[n])/3) <= abs(f[i]) < ((f[0]-f[n])/1.5):
            tortoise.color("orange", "gold")             # set turtle color
        else:
            tortoise.color("coral3", "IndianRed")        # set turtle color
        
        tortoise.begin_fill()                           # begin drawing shapes
        tortoise.left(90)
        tortoise.forward(f[i])                          # draw bar height
        tortoise.right(90)
        tortoise.forward(1/3*width)                            # prepare for text
        if f[i] >= 0:
            tortoise.write(f[i])                        # write value
        else:
            tortoise.penup()
            tortoise.right(90)
            tortoise.forward(15)
            tortoise.write(f[i])
            tortoise.forward(-15)
            tortoise.left(90)
            tortoise.pendown()
        tortoise.forward(2/3*width)                     # bar width
        tortoise.right(90)
        tortoise.forward(f[i])
        tortoise.left(90)
        tortoise.penup()
        tortoise.right(90)
        tortoise.forward(25)
        tortoise.left(90)
        tortoise.forward(-2/3*width)
        tortoise.write(w[i])                            # write word
        tortoise.forward(2/3*width)
        tortoise.left(90)
        tortoise.forward(25)
        tortoise.right(90)
        tortoise.forward(spacing)                       # spacing
        tortoise.pendown()
        tortoise.end_fill()                             # stop drawing shapes
    turtle.exitonclick()


values = sorted(dictionary.values(), reverse = True)
words = sorted(dictionary, key = dictionary.__getitem__, reverse=True)
n_freq = word_freq()
graph_word_freq(n_freq, values, words)
