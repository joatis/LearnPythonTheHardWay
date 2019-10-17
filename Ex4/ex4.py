# Assign 100 to cars
cars = 100
# assign 4.0 to space_in_a_car
space_in_a_car = 4.0
# assign drivers to 30
drivers = 30
# assign passengers to 90
passengers = 90
# assign cars_not_driven to difference 
cars_not_driven = cars - drivers
# assign cars_driven to drivers
cars_driven = drivers
# assign carpool_capacity to product
carpool_capacity = cars_driven * space_in_a_car
# assign average_passengers_per_car to dividend
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,
      "in each car.")
