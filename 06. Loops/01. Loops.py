'''
30.08.2018 19:57
Loops
'''

#For loop
print("For loop:\n")
l = [1,2,3,4,5,6]   #define list
print("l = [1,2,3,4,5,6]")
x = 0               #define x and assing value
print("x = 0")
print("for i in l: \n   x +=i")
for i in l:         #set condition for "for" loop: for every element of the list
    #"i" is called the loop variable. It can be given any name.
    x += i          #set statement for "for" loop: add every element to x
print("x =",x)      #print result of "for" loop

#While loop
print("\n\nWhile loop:\n")
t = (1,2,3,4,5,6)   #define tuple
print("t = (1,2,3,4,5,6)")
x = 0               #define x and assing value
i = 0
print("x = 0")
print("i = 0")
print("while i < len(t): \n    x += t[i] \n    i += 1")
while i < len(t):   #set condition for "while loop": as long as i < length of t
    x += t[i]       #set statement for "while" loop: add every element to x
    i += 1          #increment i with 1 every run
print("x =",x)      #print result


#Counting the number of digits in a number
print("\n\nHow many digits does a number have?")
def arguments(prompt_msg):
    while True: #create loop for error check
        try:
            variable = float(input(prompt_msg)) #convert user input to integer
        except(ValueError):
            #if input is not a number, retry
            print("invalid number, please try again:")
            continue
        else:
            #user input was valid, end
            break
    return variable

n = arguments("\nPlease input a number: ")
count = 0
print ("while n != 0: \n    count = count + 1 \n    n = n // 10")
while n != 0:
    count = count + 1
    n = n // 10
print("n has",count, "digits")

'''
Use a for loop if you know, before you start looping, the maximum number of
times that you’ll need to execute the body. For example, if you’re traversing
a list of elements, you know that the maximum number of loop iterations you
can possibly need is “all the elements in the list”. Or if you need to print
the 12 times table, we know right away how many times the loop will need to run.
'''

