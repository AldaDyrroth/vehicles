from faker import Faker
from datetime import datetime
from src.data_models.models import Generators

fake = Faker()

# Предположим, что VehicleData определен как:
from dataclasses import dataclass

@dataclass
class VehicleData:
    vin: str
    model: str
    manufacturer: str
    year: int
    odometer: int
    odometerUnit: str

# Генерация 3 автомобилей
cars = Generators.generate_vehicle_data(3)
for car in cars:
    print(car)

print(cars)



def govno(name, **params):
    for detail, value in params.items():
        print(f"{detail}: {value}")
    print(params)


govno(1, gogo=1, fifi="rrrr")