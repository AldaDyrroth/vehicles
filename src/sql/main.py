import os
import sys
import asyncio

from src.sql.queries.orm import SyncORM, AsyncORM
from src.sql.queries.core import SyncCore, AsyncCore
from tests.conftest import rndm_vehicle_id
from src.data_models.models import Generators

sys.path.insert(1, os.path.join(sys.path[0], '..'))

async def main():


    # SyncCore.select_vehicle()
    # SyncCore.insert_vehicle(2)
    # SyncCore.update_vehicle(2170, model="fsfsfds", manufacturer="drandulet")
    # SyncCore.delete_vehicle(926)


    # await AsyncCore.select_vehicle()
    # await AsyncCore.insert_vehicle(2)
    # await AsyncCore.update_vehicle(22712, model="fsfsfds", manufacturer="drandulet")
    # await AsyncCore.delete_vehicle(22713)


    # SyncORM.select_vehicles()
    # SyncORM.insert_vehicles(2)
    # SyncORM.update_vehicle(2161)
    # SyncORM.delete_vehicles(22700)


    # await AsyncORM.select_vehicles()
    # await AsyncORM.insert_vehicles(2)
    await AsyncORM.update_vehicle(2161, odometer=Generators.generate_update_data()["odometer"], odometerUnit=Generators.generate_update_data()["odometerUnit"])
    # await AsyncORM.delete_vehicles(22710)

asyncio.run(main())