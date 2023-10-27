# assigns the integer value 100 to cars.
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
# assigns the value of the result of the operation cars - drivers to cars_not_driven.
cars_not_driven = cars - drivers
# assigns the value of drivers to cars_driven.
cars_driven = drivers
# assigns the value of result of cars_driven * space_in_a_car to the variable carpool_capacity.
carpool_capacity = cars_driven * space_in_a_car
# assigns the result of the expression passengers / cars_driven to the variable on the left.
average_passengers_per_car = passengers / cars_driven

# prints the given inputs seperated by spaces.
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,
      "in each car.")
