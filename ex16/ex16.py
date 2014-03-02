# Royce Pope
# Mar 2 2014

from sys import argv
import time

script, filename = argv

print ("We are going to erase %r." % filename)
print ("If you do not want that, hit CTRL-C.")
print ("If you do want that, hit RETURN.")

input("?")

print ("Opening the file...")
print (".")
time.sleep(.5)
print ("." * 2)
time.sleep(.5)
print ("." * 3)
time.sleep(.5)
print ("." * 4)
target = open(filename, 'w')

print ("Now I am going to ask you for three lines.")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print ("I am going to write these to the file.")

target.write(line1,line2)

print ("And finally, we close it.")
target.close()