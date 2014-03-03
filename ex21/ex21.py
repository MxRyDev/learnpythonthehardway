# Royce Pope
# March 3 2014

def add(a,b):
    print ("ADDING %d + %d" % (a, b))
    return a + b

def subtract(a,b):
    print ("SUBRACTING %s - %s" % (a, b))
    return a - b

def multiply(a,b):
    print ("MULTIPLYING %d * %d" % (a, b))
    return a * b
    
def divide(a,b):
    print ("DIVIDING %d / %d" % (a, b))
    return a / b

print ("=====ADDITION=====")
print ("Please enter 1st number")    
add1 = input()
print ("Please enter 2nd number")
add2 = input()
add_answer = add(add1, add2)
print ("Addition Answer=%d" % add_answer)

'''
print ("=====SUBTRACT=====")
print ("Please enter 1st number")
sub1 = input()
print ("Please enter 2nd number")
sub2 = input()

subtract(sub1, sub2)

print ("=====MULTIPLY=====")
print ("Please enter 1st number")
mul1 = input()
print ("Please enter 2nd number")
mul2 = input()

multiply(mul1, mul2)

print ("=====DIVIDE=====")
print ("Please enter 1st number")
div1 = input()
print ("Please enter 2nd number")
div2 = input()

divide(div1, div2)
'''