# We assigned a number to the variable "cars"
cars = 100
# We assigned a number to the variable "space_in_a_car"
space_in_a_car = 4.0
# We create another variable named: drivers and passenger
drivers = 30
passengers = 90
# We create a variable that calculates the unused cars by subtracting variable "cars" with variable "drivers"
cars_not_driven = cars - drivers
# We create a variable that represents the used cars or driven cars, which is the variable "drivers"
cars_driven = drivers
# To know the capacity of the carpool we multiply the cars driven by the space in each car
carpool_capacity = cars_driven * space_in_a_car
# To know the average of passengers per car we divide the whole amount of passengers by the cars driven
average_passengers_per_car = passengers / cars_driven
#From line 17 to 22 is the printing of these variables
print("There are", cars, "cars available")
print("There are only", drivers , "drivers available")
print("There will be", cars_not_driven,"empty cars today")
print("We can transport", carpool_capacity, "people today")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car")
