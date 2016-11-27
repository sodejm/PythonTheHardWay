# Exercise 4

cars = 100
space_in_a_car = 4 #4.0 #float but not really needed since you can't have fractional people
drivers = 30
passengers = 90
cars_not_driven = cars - drivers #math with vars
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car #how much can be held

# must create another variable to deal with the undefined variable
# divide the nuber of carpool  passengers by available cars 
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
