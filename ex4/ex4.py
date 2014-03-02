# Royce Pope
# Feb 27, 2014
# Variables!

#Defining cars with a value of 100
cars = 100
#There are 4 seats in the car
space_in_a_car = 4.0
#There are a total of 30 drivers
drivers = 30
#There are a total of 90 passangers
passengers = 90
#This specifies how many cars dont have drivers
cars_not_driven = cars - drivers
cars_driven = drivers
#This specifies how much total space we have by
#multiplying the number of seats with drivers
carpool_capacity = cars_driven * space_in_a_car
#This determines how many people can fit in a car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "Therefore there will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

