import random

from pydantic import BaseModel
from typing import Optional
from typing import List
from datetime import datetime
from sqlalchemy import Table, Column, Integer, String, MetaData, Date
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import func
from src.sql.database import Base
from faker import Faker

fake = Faker()

class WorkersOrm(Base):
    __tablename__ = "Vehicles"

    id: Mapped[int] = mapped_column(primary_key=True)
    createdAt: Mapped[datetime] = mapped_column(server_default=func.now())
    vin: Mapped[str]
    model: Mapped[str]
    year: Mapped[int]
    manufacturer: Mapped[str]
    odometer: Mapped[int]
    odometerUnit: Mapped[str]

metadata_obj = MetaData()

vehicles_table = Table(
    "Vehicles",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("createdAt", Date, server_default=func.now()),
    Column("vin", String),
    Column("model", String),
    Column("year", Integer),
    Column("manufacturer", String),
    Column("odometer", Integer),
    Column("odometerUnit", String),

)



class Generators:

    @staticmethod
    def generate_vehicle_data(num_cars=1):
        cars = []
        for _ in range(num_cars):
            vehicle = VehicleData(
                vin=fake.vin(),
                model=fake.random_element(elements=("Model S", "Civic", "F-150", "Camry", "Silverado")),
                manufacturer=fake.random_element(elements=("Toyota", "Volkswagen", "Mercedes-Benz", "Ford", "Honda", "Chevrolet", "Nissan", "BMW", "Hyundai", "Kia", "Audi", "Volvo", "Subaru", "Mazda", "Lexus")),
                year=fake.random_int(min=1900, max=datetime.now().year),
                odometer=fake.random_int(min=0, max=500000),
                odometerUnit=fake.random_element(elements=("km", "mi"))
            ).model_dump()
            cars.append(vehicle)
        return cars

    @staticmethod
    def generate_update_data():

        vehicle = {
            "odometer": fake.random_int(min=0, max=500000),
            "odometerUnit": fake.random_element(elements=("km", "mi"))
        }

        return vehicle



class VehicleStock(BaseModel):
    id: int
    createdAt: datetime
    vin: str
    model: str
    manufacturer: str
    year: int
    odometer: int
    odometerUnit: str

class VehicleData(BaseModel):
    vin: str
    model: str
    manufacturer: str
    year: int
    odometer: int
    odometerUnit: str

class VehicleAds(BaseModel):
    _id: str
    vin: str
    model: str
    manufacturer: str
    year: int
    odometer: int
    odometerUnit: str
    price: float
    priceUnit: str
    publishedAt: datetime
    __v: int
