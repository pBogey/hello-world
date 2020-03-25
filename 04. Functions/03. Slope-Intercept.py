'''
Finding line slope and intercept
19.08.2018 00:59
'''

print("This program will compute a line equation y=mx+c, slope and intercept, given two points")

#Define new function for keyboard input

def arguments(prompt_msg):
    while True: #create loop for error check
        try:
            variable = float(input(prompt_msg)) #convert user input to float
        except(ValueError):
            #if input is not a number, retry
            print("invalid number, please try again:")
            continue
        else:
            #user input was valid, end
            break
    return variable

print("\nDefine points coordinates:\n")
x1 = arguments("Please input x1 value: ")
y1 = arguments("Please input y1 value: ")
x2 = arguments("Please input x2 value: ")
y2 = arguments("Please input y2 value: ")

def slope(x1,y1,x2,y2):
    m=(y2-y1)/(x2-x1)
    return m

def interceptx(x1,y1,x2,y2):
    m = slope(x1,y1,x2,y2)
    x = (m*x1-y1)/m
    return x

def intercepty(x1,y1,x2,y2):
    m=slope(x1,y1,x2,y2)
    y = -m*x1+y1
    return y

print("\nSlope of line:",slope(x1,y1,x2,y2))
print("X intercept:",interceptx(x1,y1,x2,y2))
print("Y intercept:",intercepty(x1,y1,x2,y2))



