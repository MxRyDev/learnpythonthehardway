# Royce Pope
# Feb 28 2014

name = raw_input("What is your name?> ")
age = raw_input("How old are you?> ")
gender = raw_input("What is your Gender?> ")

print "*" * 30
print "Is this information correct?"
print "Name: ", name
print "Age: ", age
print "Gender: ", gender
submit = raw_input("Submit?(Y/N)> ")

if submit == "Y":
    print "Your information has been submitted."
    print "Thank You!"
    
else:
    print "Your information has not been submitted."
    print "Goodbye"
    
  