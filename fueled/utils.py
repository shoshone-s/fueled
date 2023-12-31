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
    def __init__(self, distance, units='mi', city_driving=0.55):
        self.distance = int(distance)
        if units=='mi':
            self.units = units
        elif units=='km':
            self.units = 'km'
        else:
            self.units = 'mi'
        self.city_driving = float(city_driving)
        self.hwy_driving = round(1 - city_driving, 2)
    def __str__(self):
        return f'Trip:\t{self.distance} {self.units}, {self.city_driving}% city driving {self.hwy_driving}% hwy driving'

    # unit conversion methods
    def milesToKilometers(self):
        kilometers=self.distance * 1.60934
        return round(kilometers, 1)
    def kilometersToMiles(self):
        miles=self.distance * 0.621371
        return round(miles, 1)


# vehicle class
class Vehicle:
    def __init__(self, year, make, model, transmission='automatic'):
        self.year = int(year)
        self.make = str(make.capitalize())
        self.model = str(model.capitalize())
        self.transmission = str(transmission.capitalize())
    def __str__(self):
        return f'Vehicle:\t{self.year} {self.make} {self.model}\n Transmission: {self.transmission}'

    # vehicle specs method
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
        
    # fuel consumption method
    def fuelConsumption(self, trip):
        # get tip info
        city_miles = trip.distance * trip.city_driving
        hwy_miles = trip.distance * trip.hwy_driving
        # get vehicle specs
        vehicle_info=self.specs()
        payload=[]
        # if trip is in miles
        if trip.units == 'mi':
            for vehicle_record in vehicle_info:
                city_consumption = city_miles/vehicle_record['city_mpg_fuel1']
                hwy_consumption = hwy_miles/vehicle_record['hwy_mpg_fuel1']
                vehicle_record['est_consumption_gal']= round(city_consumption + hwy_consumption, 2)
                payload.append(vehicle_record)
        # if trip is in kilometer
        elif trip.units == 'ki':
            for vehicle_record in vehicle_info:
                city_consumption = city_miles/vehicle_record['city_mpg_fuel1']
                hwy_consumption = hwy_miles/vehicle_record['hwy_mpg_fuel1']
                vehicle_record['est_consumption_gal']= round(city_consumption + hwy_consumption, 2)
                vehicle_record['est_consumption_km']=round(city_consumption + hwy_consumption, 2)
                payload.append(vehicle_record)
        else:
            return 'err calculating fuel consumption'
        
        return payload
        