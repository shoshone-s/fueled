"""
    This file should contain all the functions related to calculations and data handling
"""
from utils import Vehicle, Trip

# delete this import later
from pprint import pprint

car1 = Vehicle(2000, 'Ford', 'e150')
trip1 = Trip(120, 'miles')

pprint(car1.specs())

# kilometers = trip1.milesToKilometers()
# car_info=car1.specs()
# print(car1)
# print(kilometers)
# pprint(car_info)
# vehicle fuel mileage
# amount of fuel needed
# 
