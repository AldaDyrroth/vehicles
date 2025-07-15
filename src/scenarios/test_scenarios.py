
from src.api.api_client import VehicleApiClient
import os
import sys
from src.sql.queries.orm import AsyncORM
from faker import Faker
import time

fake = Faker()

sys.path.insert(1, os.path.join(sys.path[0], '..'))


class TestScenarios:
    def __init__(self, client: VehicleApiClient): # Типизация для ясности
        self.session_vehicle_id = None
        self.client = client

    async def creation_vehicle_and_delete(self, vehicle_data):
        """
        Сценарий: создать vehicle, проверить доступность по API и сразу же его удалить.
        Возвращает ID созданного и удаленного vehicle.
        """
        created_vehicle_data = self.client.create_vehicle(vehicle_data)
        vehicle_id = created_vehicle_data.get("id")
        assert vehicle_id is not None, f"ID не найден в ответе на создание: {created_vehicle_data}"

        get_new_vehicle = self.client.get_stock_id(vehicle_id)
        print(f"Vehicle с ID {vehicle_id} доступен по API.", end=" ")

        await AsyncORM.delete_vehicles(vehicle_id)

        print(f"Vehicle с ID {vehicle_id} успешно создан и удален напрямую из БД.")
        self.session_vehicle_id = vehicle_id
        return vehicle_id



    def error_creation_vehicle(self, vehicle_data):
        """
        Сценарий: создать vehicle с неверным телом запроса.
        Возвращает status-code.
        """
        params = [key for key in set(vehicle_data)]
        el = fake.random_element(params)
        vehicle_data.pop(el)
        self.client.create_vehicle_noval(400, vehicle_data)

        print(f"Vehicle не создан из-за отсутствия поля {el}.")



    def creation_ads_announcement(self, vehicle_data):
        """
        Сценарий: создать vehicle и cпустя 30сек проверить наличие объявления в ads.
        Возвращает ID созданного vehicle и его объявления в ads.
        """
        created_vehicle_data = self.client.create_vehicle(vehicle_data)
        vehicle_id = created_vehicle_data.get("id")
        assert vehicle_id is not None, f"ID не найден в ответе на создание: {created_vehicle_data}"
        time.sleep(30)

        created_ads_data = self.client.get_ads_id(vehicle_id)

        print(f"Объявление для vehicle с ID {vehicle_id} успешно создано.")
        return created_ads_data



    def get_and_verify_stocks_exist(self):
        """
        Сценарий: получить список vehicles и проверить, что он не пуст.
        """
        vehicles = self.client.get_stock()
        assert len(vehicles) > 0, "Список vehicles пуст"
        print(f"Получено {len(vehicles)} vehicles.")
        return vehicles



    def get_and_verify_ads_exist(self):
        """
        Сценарий: получить список ads и проверить, что он не пуст.
        """
        ads = self.client.get_ads()
        assert len(ads) > 0, "Список объявлений пуст"
        print(f"Получено {len(ads)} объявлений.")
        return ads