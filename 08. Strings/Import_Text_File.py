"""
Strings
29.10.2018 19:32
Bogdan Prădatu
"""


punctuation = "~!@#$%^&*()_-=+[{]}\\|'\";:,<.>/?"


def remove_punctuation(text):
    text_wo_punctuation = ""
    for word in text:
        if word not in punctuation:
            text_wo_punctuation += word
    return text_wo_punctuation


with open(r'New Text Document.txt') as f:
    text = f.read().lower()
    t = remove_punctuation(text).split()
    dictionary = {}
    for word in t:
        if word in dictionary:
            dictionary[word] = dictionary[word] + 1
        else:
            dictionary[word] = 1


def top_five(d):
    top = {}
    value1 = 0
    value2 = 0
    value3 = 0
    value4 = 0
    value5 = 0

    for key in dictionary:
        if value1 < dictionary[key] and key not in top:
            value1 = dictionary[key]
            top1 = {key: value1}
        else:
            continue
    top.update(top1)    
    for key in dictionary:
        if value2 < dictionary[key] and key not in top:
            value2 = dictionary[key]
            top2 = {key: value2}
        else:
            continue
    top.update(top2)
    for key in dictionary:
        if value3 < dictionary[key] and key not in top:
            value3 = dictionary[key]
            top3 = {key:value3}
        else:
            continue
    top.update(top3)
    for key in dictionary:
        if value4 < dictionary[key] and key not in top:
            value4 = dictionary[key]
            top4 = {key:value4}
        else:
            continue
    top.update(top4)
    for key in dictionary:
        if value5 < dictionary[key] and key not in top:
            value5 = dictionary[key]
            top5 = {key:value4}
        else:
            continue
    top.update(top5)
    return top


print(top_five(dictionary))


import turtle                               # import turtle module
window = turtle.Screen()                    # create screen
window.bgcolor("honeydew")                  # define screen color
window.title("Bar Chart")                   # set window title
turtle.screensize(500,500)                  # set window size
tortoise = turtle.Turtle()                  # create turtle
tortoise.hideturtle()                       # hide turtle stamp
tortoise.penup()                            # raise turtle pen
tortoise.setposition(-200,-200)             # position turtle
tortoise.pendown()                          # put turtle pen down
tortoise.speed(5)                           # set drawing speed


def draw_bar_chart(t,h,w):                          # create function to draw chart
    """draw a bar chart, based on given data."""
    if abs(h) < 100:
        tortoise.color("SeaGreen","ForestGreen")    # set turtle color
    elif abs(h) >= 100 and abs(h) < 200:
        tortoise.color("orange","gold")             # set turtle color
    else:
        tortoise.color("coral3","IndianRed")        # set turtle color
    
    t.begin_fill()                          # begin drawing shapes
    t.left(90)
    t.forward(h)                            # draw bar height
    t.right(90)
    t.forward(20)                           # prepare for text
    if h >= 0:
        t.write(h)                          # write value
    else:
        t.penup()
        t.right(90)
        t.forward(15)
        t.write(h)
        t.forward(-15)
        t.left(90)
        t.pendown()
    t.forward(40)                           # bar width
    t.right(90)
    t.forward(h)
    t.left(90)
    t.penup()
    t.right(90)
    t.forward(15)
    t.left(90)
    t.forward(-50)
    t.write(w)                              # write word
    t.forward(50)
    t.left(90)
    t.forward(15)
    t.right(90)
    t.forward(20)                           # spacing
    t.pendown()
    t.end_fill()                            # stop drawing shapes


top = top_five(dictionary)
words=list(top)
i = 0


for key in top:
    draw_bar_chart(tortoise,top[key],words[i])
    i += 1


turtle.exitonclick()
