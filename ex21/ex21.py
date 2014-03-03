# Royce Pope
# March 3 2014
# Simple Calculator v1.1

def add(a,b):
    print ("=====ADDITION=====")
    print ("ADDING %d + %d" % (a, b))
    return a + b
    
def subtract(a,b):
    print ("=====SUBTRACT=====")
    print ("SUBRACTING %d - %d" % (a, b))
    return a - b

def multiply(a,b):
    print ("=====MULTIPLY=====")
    print ("MULTIPLYING %d * %d" % (a, b))
    return a * b
    
def divide(a,b):
    print ("=====DIVIDE=====")
    print ("DIVIDING %d / %d" % (a, b))
    return a / b
    
print ("""
******************************
*                            *
*          WELCOME TO        *
*         ROYCE POPE'S       *
*      SIMPLE CALCULATOR     *
*                            *
****************************** \n""")

print ("Let's do some Math!")

print("""
What would you like to do?
1) Addition     3) Multiplication
2) Subtraction  4) Division
""")

choice = int(input(">> "))

print ("Please enter 1st number")    
num1 = int(input(">> "))
print ("Please enter 2nd number")
num2 = int(input(">> "))

if choice == 1:
    answer = add(num1, num2)
    print ("Answer = %s" % answer)

if choice == 2:
    answer = subtract(num1, num2)
    print ("Answer = %s" % answer)
     
if choice == 3:
    answer = multiply(num1, num2)
    print ("Answer = %s" % answer)

if choice == 4:
    answer = divide(num1, num2)
    print ("Answer = %s" % answer)