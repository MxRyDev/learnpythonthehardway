# Royce Pope
# March 3 2014
# Simple Calculator

def add(a,b):
    print ("ADDING %d + %d" % (a, b))
    return a + b

def subtract(a,b):
    print ("SUBRACTING %d - %d" % (a, b))
    return a - b

def multiply(a,b):
    print ("MULTIPLYING %d * %d" % (a, b))
    return a * b
    
def divide(a,b):
    print ("DIVIDING %d / %d" % (a, b))
    return a / b

print ("=====ADDITION=====")
print ("Please enter 1st number")    
add1 = int(input(">> "))
print ("Please enter 2nd number")
add2 = int(input(">> "))
add_answer = add(add1, add2)
print ("Answer = %d" % add_answer)

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