# todo: delete this import later
from pprint import pprint


# imports
# from dotenv import load_dotenv
# load_dotenv()
# import os
import json
# functions:
# ----------
# function for finding missing vehicle informations
# def findVehicleInfo(vehicle):
#     # import
#     return ''



# classes
# class for trips (this will be from user input)
class Trip:
    def __init__(self, distance, units='miles'):
        self.distance = int(distance)
        self.units = str(units.capitalize())
    # dunder str function for returning trip details (as of now, just returning the details)
    def __str__(self):
        return f'Trip:\t{self.distance} {self.units}'

    # unit conversion methods
    def milesToKilometers(self):
        kilometers=self.distance * 1.60934
        return round(kilometers, 1)
    def kilometersToMiles(self):
        miles=self.distance * 0.621371
        return round(miles, 1)

# class for vehicle (this will be from user input)
class Vehicle:
    def __init__(self, year, make, model, transmission='automatic'):
                # for the time being, removing these attrs
                #  , vehicle_class=None, fuel_type=None, fuel_capacity=None):
        self.year = int(year)
        self.make = str(make.capitalize())
        self.model = str(model.capitalize())
        self.transmission = str(transmission.capitalize())
        # # if fuel type is input, return it, otherwise return '...'
        # if fuel_type:
        #     self.fuel_type = str(fuel_type.capitalize())
        # else:
        #     self.fuel_type = '...'
        # # if vehicle class is input, return it, otherwise return '...'
        # if vehicle_class:
        #     self.vehicle_class = str(vehicle_class.upper())
        # # elif not vehicle_class:
        # #     self.vehicle_class = 'looking for fuel capacity'
        # else:
        #     self.vehicle_class='...'
        # # if fuel capacity is input, return it, otherwise return '...'
        # if fuel_capacity:
        #     self.fuel_capacity = int(fuel_capacity)
        # # elif not fuel_capacity:
        # #     self.fuel_capacity = 'looking for fuel capacity'
        # else:
        #     self.fuel_capacity = '...'
    # dunder str function for returning trip details (as of now, just returning the details)
    def __str__(self):
        return f'Vehicle:\t{self.year} {self.make} {self.model}\n Transmission: {self.transmission}'
        # \nVehicle Class:\t{self.vehicle_class}\nFuel Type:\t{self.fuel_type}\nFuel Capacity:\t{self.fuel_capacity}'

    # function for finding vehicle info
    def specs(self):
        # init list for vehicles matching description
        found_vehicles=[]
        try:
            # check to see if the vehicle info is in 'vehicles.json'
            with open('data/vehicles.json', 'r') as source_file:
                source_file_data = json.load(source_file)
                for vehicle in source_file_data:
                    if (self.year == vehicle['year']) and (self.make in vehicle['make']) and (self.model in vehicle['model']):
                        found_vehicles.append(vehicle)
                    else:
                        pass
        except Exception as err:
            return err
        finally:
            if found_vehicles:
                return found_vehicles
            else:
                return f"Sorry, no '{self.year} {self.make} {self.model}' found"

        # if len(found_vehicles)>0:
        #     return found_vehicles
        # else:
        #     return 'vehiclenot found'
        
        
    # function for calculating the fuel consumption of a vehicle
    def fuelConsumption(self):
        pass

# class FuelCalc:
#     def __init__(self, speed):


# class Distance: