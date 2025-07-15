from sqlalchemy import insert, select, update, delete

from src.sql.database import Engines
from src.data_models.models import metadata_obj, vehicles_table, Generators


class SyncCore:

    @staticmethod
    def insert_vehicle(count):
        with Engines.sync_engine.connect() as conn:
            stmt = insert(vehicles_table).values(
                    Generators.generate_vehicle_data(count)
            )
            conn.execute(stmt)
            conn.commit()

    @staticmethod
    def select_vehicle():
        with Engines.sync_engine.connect() as conn:
            query = select(vehicles_table)#.filter_by()
            result = conn.execute(query)
            vehicles = result.scalars().all()[-1]
            print(f"{vehicles=}")

    @staticmethod
    def update_vehicle(rndm_vehicle_id, **params):
        with Engines.sync_engine.connect() as conn:
            # stmt = text("UPDATE public.\"Vehicles\" SET odometer=:new_odometer WHERE id=:id")
            # stmt = stmt.bindparams(
            #     new_odometer=odometer,
            #     id=id
            # )
            stmt = (
                update(vehicles_table)
                .values(params)
            #    .where(vehicles_table.c.id==id)
                .filter_by(id=rndm_vehicle_id)
            )
            conn.execute(stmt)
            conn.commit()

    @staticmethod
    def delete_vehicle(id: int):
        with Engines.sync_engine.connect() as conn:
            down = (
                delete(vehicles_table)
                .filter_by(id=id)
            )
            conn.execute(down)
            conn.commit()

class AsyncCore:

    @staticmethod
    async def insert_vehicle(count):
        async with Engines.async_engine.connect() as conn:
            stmt = insert(vehicles_table).values(
                Generators.generate_vehicle_data(count)
            )
            await conn.execute(stmt)
            await conn.commit()

    @staticmethod
    async def select_vehicle():
        async with Engines.async_engine.connect() as conn:
            query = select(vehicles_table)
            result = await conn.execute(query)
            vehicles = result.scalars().all()[-1]
            print(f"{vehicles=}")

    @staticmethod
    async def update_vehicle(id: int, **params):
        async with Engines.async_engine.connect() as conn:
            stmt = (
                update(vehicles_table)
                .values(params)
                #    .where(vehicles_table.c.id==id)
                .filter_by(id=id)
            )
            await conn.execute(stmt)
            await conn.commit()

    @staticmethod
    async def delete_vehicle(id: int):
        async with Engines.async_engine.connect() as conn:
            down = (
                delete(vehicles_table)
                .filter_by(id=id)
            )
            await conn.execute(down)
            await conn.commit()