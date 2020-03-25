'''
Expressions/Operations
08.08.2018 21:05

Order of operations: PEMDAS
Parentheses
Exponentiation
Multiplication & Division
Addition & Subtraction
'''
print ("Understand operations in python")

#Define variables
print ("\nDefine variables:")
a = 5 #assign 100 to var a
print("a=",a)
b = 2 #assign 99 to var b
print("b=",b,"\n")

print("********** Arithmetic Operators **********")
print("Unary Positive \n +a =", +a)
print("Unary Negative \n -a =", -a)
print("Addition \n  a+b=",a+b)
print("Substraction \n  a-b=",a-b)
print("Multiplication \n  a*b=",a*b)
print("Division \n  a/b=",a/b)
print("Exponentiation \n  a**b=",a**b)
print("Modulo \n  a%b=",a%b)
print("  extract last digits of number:","\n    5467%10 =", 5467%10, "\n    5467%100=",5467%100 )
print("Floor Division \n  a//b=",a//b,"\n")

print("a==(a//b)*b+(a%b) =",(a//b)*b+(a%b),"\n")

print("Invert \n  ~a=",~a)
print("  ~b=",~b,"\n")

print("********** Comparison Operators **********")
print("Equal to \n a==b :", a==b)
print("Not equal to \n a!=b :", a!=b)
print("Greater than \n a>=b :", a>b)
print("Greather than or equal to \n a>=b :", a>=b)
print("Less than \n a<b :", a<b)
print("Less than or equal to \n a<=b :", a<=b)

'''
String Operations: Addition & Multiplication
'''
#Define Strings
print("\nString operations")
word1="Hello, " #assign string to variable word1
print("word1=",word1)
word2="World!"  #assign string to variable word1
print("word2=",word2)
message1 = word1+word2
message2 = message1*2
print("\nmessage1 = word1+word2 \n  ",message1)
print("\nmessage2 = message1*2 \n  ",message2)
