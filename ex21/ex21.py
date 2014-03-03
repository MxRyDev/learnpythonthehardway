# Royce Pope
# March 3 2014
# Simple Calculator v1.0

import os

def add(a,b):
    print ("=====ADDITION=====")
    ans = add(num1, num2)
    print ("ADDING %d + %d" % (a, b))
    print ("Answer = %d" % ans)
    return a + b
    
print ("""
******************************
*                            *
*          WELCOME TO        *
*         ROYCE POPE'S       *
*      SIMPLE CALCULATOR     *
*                            *
****************************** \n""")

print("""
What would you like to do?
1) Addition
2) Subtraction
3) Multiplication
4) Division
""")

choice = int(input(">> "))

print ("Please enter 1st number")    
num1 = int(input(">> "))
print ("Please enter 2nd number")
num2 = int(input(">> "))

if choice == 1:
    os.system('clear')
    output = add(num1, num2)

if choice == 2:
    subtract()
def subtract(a,b):
    print ("SUBRACTING %d - %d" % (a, b))
    return a - b

def multiply(a,b):
    print ("MULTIPLYING %d * %d" % (a, b))
    return a * b
    
def divide(a,b):
    print ("DIVIDING %d / %d" % (a, b))
    return a / b

print ("Let's do some Math!")

print ("=====SUBTRACT=====")
print ("Please enter 1st number")
sub1 = int(input(">> "))
print ("Please enter 2nd number")
sub2 = int(input(">> "))
sub_answer = subtract(sub1, sub2)
print ("Answer = %d" % sub_answer)

print ("=====MULTIPLY=====")
print ("Please enter 1st number")
mul1 = int(input(">> "))
print ("Please enter 2nd number")
mul2 = int(input(">> "))
mul_answer = multiply(mul1, mul2)
print ("Answer = %d" % mul_answer)

print ("=====DIVIDE=====")
print ("Please enter 1st number")
div1 = int(input(">> "))
print ("Please enter 2nd number")
div2 = int(input(">> "))
div_answer = divide(div1, div2)
print ("Answer = %d" % div_answer)