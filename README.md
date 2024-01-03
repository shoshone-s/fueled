# **Fueled**

The **_fueled_** package is a Python library designed to assist in calculating and managing vehicle gas mileage, providing
functionalities to compute fuel consumption, mileage, and perform unit conversions.

## **Features**

- Calculate fuel consumption based on distance and MPG (miles per gallon).
- Support for both city and highway MPG values.
- Convert between different units of measurement for mileage and fuel consumption.

## **Installation**

You can install the package via pip:

```bash
pip install fueled
```

## **Usage**

### Vehicle and Trip objects

### _<ins>Vehicle:</ins>_

##### Attributes:

- **_year_**
    - This is the year of the vehicle

        - Mandatory attribute

- **_make_**
    - This is the manufacturer/manufacturing company of the vehicle

        - Mandatory attribute

- **_model_**
    - This is the specific model of the vehicle

        - Mandatory attribute

- **_transmission_**
    - This is the type of transmission that the vehicle has

    - The two options for this attribute are currently 'automatic' or 'manual'

    - The default value will be 'automatic' if no other value is chosen

    - Optional attribute

##### Methods:
- **_specs()_** 
    - Function that returns a list of all the vehicles and specifications that match the year, make and model of the vehicle instance

    - Takes no input values

- **_fuelConsumption(_** <ins>trip</ins> **_)_** 
    - Function that calculates the fuel consumption of the vehicle instance. It will return a list of vehicles that match the year, make and model of the vehicle instance

    - Takes in a _trip_ object instance to calculate the fuel consumption

### _<ins>Trip:</ins>_

##### Attributes:

- **_distance_**
    - This is the total distance of the trip (miles or kilometers)

        - Mandatory attribute

- **_units_**
    - This is the unit of measurement that should (for miles - 'mi' / for kilometers - 'km')
        
        - The defualt value for _units_ is miles - 'mi'
        
        - Optional attribute

- **_city_driving_**
    - This is the amount of city driving that for the trip instance
    
    - Measured as a percentage value that is represented as a positive float less than the whole number 1

    - The default value for city driving is '0.55' or 55%

        - It can be assumed that the difference between 1 and the city driving, will be the amount of highway driving
        #### Example:
        ```python
            # Trip instance
            trip1 = Trip(distance=120, units='mi', city_driving=0.40)
            print(f'City Driving: {trip1.city_driving}')
            print(f'Highway Driving: {trip1.hwy_driving}')
        ```
        ```bash
        City Driving: 0.40
        Highway Driving: 0.60
        ```

##### Methods:
- **_milesToKilometers()_**
    - Function for converting trip in miles to kilometers

    - Takes no input values

- **_kilometersToMiles()_**
    - Function for converting the trip in kilometers to miles

    - Takes no input values

<!-- ### Calculating Fuel Consumption -->
### Example
1. Import the 'Vehicle' and 'Trip' classes
2. Create vehicle and trip instances
3. Using the 'fuelConsumption()' method from 'Vehicle', calculate the fuel consumption of the vehicle instance
    <!-- - Vehicle must have the 'year', 'make' and 'model' attributes to create a vehicle instance (the 'transmission' attribute is optional and will default to 'automatic' if user does not define it as 'automatic' or 'manual') **Note** 'automatic' or 'manual' are currently the only accepted options
    - Trip must have the 'distance' attribute to create a trip instance (the 'units' and 'city_driving' attributes are optional; 'units' will default to 'mi' - ("miles") if user does not define it as 'mi' - ("miles") or 'ki' ("kilometers") / 'city_driving' will default to '55%' or '0.55' if not defined and should always be a positive decimal less than 1) -->

```python
from fueled import Vehicle, Trip

# Provide the vehicle's details
car = Vehicle(year=2000, make='Ford', model='E150')

# Provide inputs for the trip's total distance, units of measurement and percentage of city and highway driving
trip = Trip(distance=100, units='km', city_driving=0.55)

# Call the 'fuelConsumption' method from the vehicle instance and provide the trip object to calculate the fuel consumption
fuel_consumption = car.fuelConsumption(trip)
```
```bash
[{'_id': '16206',
  'alt_fuel': 'none',
  'city_mpg_fuel1': 13,
  'city_mpg_fuel2': 0,
  'combined_mpg_fuel1': 15,
  'combined_mpg_fuel2': 0,
  'cylinders': '8',
  'displacement': '4.6',
  'displacement_measure': 'liters',
  'drivetrain': 'Rear-Wheel Drive',
  'eng_id': '0',
  'est_consumption_gal': 6.47,
  'fuel_source': 'single fuel',
  'fuel_type': 'Regular',
  'has_mpg_data': 'Y',
  'hwy_mpg_fuel1': 17,
  'hwy_mpg_fuel2': 0,
  'make': 'Ford',
  'model': 'E150 Club Wagon',
  'primary_fuel': 'Regular Gasoline',
  'sub_cat': 'Vans, Passenger Type',
  'transmission': 'Automatic 4-spd',
  'year': 2000},
 {'_id': '16207',
  'alt_fuel': 'none',
  'city_mpg_fuel1': 12,
  'city_mpg_fuel2': 0,
  'combined_mpg_fuel1': 13,
  'combined_mpg_fuel2': 0,
  'cylinders': '8',
  'displacement': '5.4',
  'displacement_measure': 'liters',
  'drivetrain': 'Rear-Wheel Drive',
  'eng_id': '0',
  'est_consumption_gal': 7.42,
  'fuel_source': 'single fuel',
  'fuel_type': 'Regular',
  'has_mpg_data': 'Y',
  'hwy_mpg_fuel1': 16,
  'hwy_mpg_fuel2': 0,
  'make': 'Ford',
  'model': 'E150 Club Wagon',
  'primary_fuel': 'Regular Gasoline',
  'sub_cat': 'Vans, Passenger Type',
  'transmission': 'Automatic 4-spd',
  'year': 2000}]
```


