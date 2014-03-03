# Royce Pope
# March 3 2014

# Defined a function named cheese_and_crackers with two arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print ("You have %d cheeses!" % cheese_count)
    print ("You have %d boxes of crackers!" % boxes_of_crackers)
    print ("Man that's enough for a party!")
    print ("Get a blanket.\n")
    
print ("We can just give the functions numbers directly:")
# Giving our two function variables numbers.
cheese_and_crackers(20, 30)

print ("Or, we can use variables from our script:")
# Defined two variables
amount_of_cheese = 10
amount_of_crackers = 50

# Using the two defined variables in the function
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print ("We can even do math inside too:")
# Giving some math to the function
cheese_and_crackers(10 + 20, 5 + 6)

print ("And we can combine the two, variables and math:")
# Combining variables and math to the function
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)