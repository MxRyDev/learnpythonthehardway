# Royce Pope
# March 3 2014

def add(a,b):
    print ("ADDING %d + %d" % (a, b))
    return a + b
    print ("%d" % add)

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

number = add(5, 5)

print ("Addition Answer=%d" % number)

print ("=====SUBTRACTION=====")
print ("Please enter 1st number")
sub1 = input()
print ("Please enter 2nd number")
sub2 = input()

subtract(sub1, sub2)