from sqlalchemy import text, insert, delete, select, update

from src.sql.database import Engines
from src.data_models.models import metadata_obj, WorkersOrm, vehicles_table, Generators


class SyncORM:

    @staticmethod
    def select_vehicles():
        with Engines.sync_session_factory() as session:
            #select = session.get(WorkersOrm, vehicle_id)
            query = select(WorkersOrm)# .filter_by()
            result = session.execute(query)
            vehicles = result.scalars().all()
            print(f"{vehicles=}")

    @staticmethod
    def insert_vehicles(count):
        with Engines.sync_session_factory() as session:
            data = Generators.generate_vehicle_data(count)
            total = []
            for i in range(count):
                vehicle = WorkersOrm(
                    vin=data[i]["vin"],
                    model=data[i]["model"],
                    manufacturer=data[i]["manufacturer"],
                    year=data[i]["year"],
                    odometer=data[i]["odometer"],
                    odometerUnit=data[i]["odometerUnit"],
                )
                total.append(vehicle)
            session.add_all(total)
            session.commit()

    @staticmethod
    def update_vehicle(id: int, new_odometer: int = 0):
        with Engines.sync_session_factory() as session:
            vehicle = session.get(WorkersOrm, id)
            vehicle.odometer = new_odometer
            session.commit()

    @staticmethod
    def delete_vehicles(vehicle_id):
        with Engines.sync_session_factory() as session:
            session.query(WorkersOrm).filter_by(id=vehicle_id).delete()
            session.commit()



class AsyncORM:

    @staticmethod
    async def select_vehicles(**wheres):
        async with Engines.async_session_factory() as session:
            # select = session.get(WorkersOrm, vehicle_id)
            query = select(WorkersOrm)  # .filter_by()
            result = await session.execute(query)
            vehicles = result.scalars().all()
            # print(f"{vehicles=}")
            print("\n" + "=" * 50)
            print(f"Найдено транспортных средств: {len(vehicles)}")
            for i, vehicle in enumerate(vehicles, 1):
                print(f"\nТС #{i}:")
                for key, value in vars(vehicle).items():
                    if not key.startswith('_'):
                        print(f"  {key}: {value}")
            print("=" * 50 + "\n")

    @staticmethod
    async def insert_vehicles(count):
        async with Engines.async_session_factory() as session:
            data = Generators.generate_vehicle_data(count)
            total = []
            for i in range(count):
                vehicle = WorkersOrm(
                    vin=data[i]["vin"],
                    model=data[i]["model"],
                    manufacturer=data[i]["manufacturer"],
                    year=data[i]["year"],
                    odometer=data[i]["odometer"],
                    odometerUnit=data[i]["odometerUnit"],
                )
                total.append(vehicle)
            session.add_all(total)
            await session.commit()

    @staticmethod
    async def update_vehicle(id: int, **params):
        async with Engines.async_session_factory() as session:
            await session.execute(
                update(WorkersOrm)
                .values(params)
                #    .where(vehicles_table.c.id==id)
                .filter_by(id=id)
            )
            await session.commit()



    @staticmethod
    async def delete_vehicles(vehicle_id):
        async with Engines.async_session_factory() as session:
            await session.execute(
                delete(WorkersOrm)
                .filter_by(id=vehicle_id)
            )
            await session.commit()