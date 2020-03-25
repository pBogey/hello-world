'''
Defining custom functions
09.08.2018 21:40
'''

print("this program will compute a line equation y=mx+c")

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

m = arguments("Please input m value: ")
x = arguments("Please input x value: ")
c = arguments("Please input c value: ")

def function(m,x,c):
    y = m*x+c
    print("y = mx+c =",y)

function(m,x,c)


