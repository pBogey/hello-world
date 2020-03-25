'''
Booleans and Logical operators
15.08.2018 17:04
'''
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

x = arguments("Please input x value: ")
y = arguments("Please input y value: ")

#Booleans
    #Equal
if x == y:
    print("\n(x==y): x is equal to y")

    #Not Equal
if x != y:
    print("\n(x!=y): x is not equal to y")

    #Greater
if x != y and x > y:
    print("          \n(x>y) : x is greater than y")

    #Less
if x != y and x < y:
    print("          \n(x<y) : x is less than y")

    #Greater than or equal
if (x == y and x >= y) or (x != y and x >= y):
    print("          \n(x>=y): x is greater than or equal to y")

    #Less than or equal
if (x == y and x <= y) or (x != y and x <= y):
    print("          \n(x<=y): x is less than or equal to y")

    #Range for x
if 0 <= x <= 100:
    print("          \n(0 <= x <= 100): x belongs to [0:100]")
elif -100 <= x <= 0:
    print("          \n(-100 <= x <= 0): x belongs to [-100:0]")
else:
    print("          \nx is greater than Abs(100)")

    #Even or Odd
if x%2==0:
    print("          \n(x%2==0): x is an even number")
elif not x%2==0 and x%3==0:
    print("          \n(not x%2==0 and x%3==0): x is an odd number and is divisible by 3")
else:
    print("          \n(not x%2==0): x is an odd number, but is not divisible by 3")

    #Range for y
if -10 < y < 10:
    print("          \ny is a single digit number")
elif -100 < y < 100:
    print("          \ny is a double digit number")
else:
    pass


    

    

