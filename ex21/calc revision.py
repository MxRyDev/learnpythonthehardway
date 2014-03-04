# Max Hayes
# March 3 2014
# Revision of 'Simple Calulator'

def get_numbers():
    num_1 = input("Please enter your first number \n>")
    num_2 = input("Please enter your second number \n>")
    return(num_1, num_2)

def add():
    print ("=====ADDITION=====")
    a,b = get_numbers()
    print ("ADDING %s + %s" % (a, b))
    return int(a) + int(b)

def subtract():
    print ("=====SUBTRACT=====")
    a,b = get_numbers()
    print ("SUBRACTING %s - %s" % (a, b))
    return int(a) - int(b)

def multiply():
    print ("=====MULTIPLY=====")
    a,b = get_numbers()
    print ("MULTIPLYING %s * %s" % (a, b))
    return int(a) * int(b)
    
def divide():
    print ("=====DIVIDE=====")
    a,b = get_numbers()
    print ("DIVIDING %s / %s" % (a, b))
    return int(a) / int(b)

choices = ['add', 'subtract', 'multiply', 'divide']

while True:
    print('''
          :::::::::::::::::::::::::::::::::::::::
          Welcome to Royces Calculator:
        please select from the following options:''')
    for i in choices:
        print(">" + i)
    choosen = input()
    if choosen in choices:
        break
    else:
        print("Sorry, That was not a valid entry...")

function = choices.index(choosen)

if function == 0: #add
    answer = add()
    
elif function == 1: #subtract
    answer = subtract()
    
elif function == 2: #multiply
    answer = multiply()
    
elif function == 3: #divide
    answer = divide()
    
else:
    print("Sorry, there has been a error. Please restart program")
    
print("....... \nThe answer is: " + str(answer))


