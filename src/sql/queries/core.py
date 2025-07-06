from sqlalchemy import text, insert, select, update, delete
from src.sql.database import sync_engine, async_engine
from src.data_models.models import metadata_obj, vehicles_table, Generators


async def get_async():
    async with async_engine.connect() as conn:
        res1 = await conn.execute(text("SELECT 1,2,3"))
        print(f'{res1.first()=}')

    def get_sync():
        with sync_engine.connect() as conn:
            res = conn.execute(text("SELECT 1,2,3"))
            print(f'{res.first()=}')

class SyncCore:

    @staticmethod
    def insert_vehicle(count):
        with sync_engine.connect() as conn:
            stmt = insert(vehicles_table).values(
                    Generators.generate_vehicle_data(count)
            )
            conn.execute(stmt)
            conn.commit()

    @staticmethod
    def select_vehicle():
        with sync_engine.connect() as conn:
            query = select(vehicles_table)#.filter_by()
            result = conn.execute(query)
            vehicles = result.scalars().all()[-1]
            print(f"{vehicles=}")

    @staticmethod
    def update_vehicle(rndm_vehicle_id, **params):
        with sync_engine.connect() as conn:
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
        with sync_engine.connect() as conn:
            down = (
                delete(vehicles_table)
                .filter_by(id=id)
            )
            conn.execute(down)
            conn.commit()

class AsyncCore:

    @staticmethod
    async def insert_vehicle(count):
        async with async_engine.connect() as conn:
            stmt = insert(vehicles_table).values(
                Generators.generate_vehicle_data(count)
            )
            await conn.execute(stmt)
            await conn.commit()

    @staticmethod
    async def select_vehicle():
        async with async_engine.connect() as conn:
            query = select(vehicles_table)
            result = await conn.execute(query)
            vehicles = result.scalars().all()[-1]
            print(f"{vehicles=}")

    @staticmethod
    async def update_vehicle(id: int, **params):
        async with async_engine.connect() as conn:
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
        async with async_engine.connect() as conn:
            down = (
                delete(vehicles_table)
                .filter_by(id=id)
            )
            await conn.execute(down)
            await conn.commit()