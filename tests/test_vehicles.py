import pytest
import random

from src.scenarios.test_scenarios import TestScenarios
from src.api.api_client import VehicleApiClient
from src.data_models.models import Generators

from src.enums.api_enums import Endpoint


@pytest.fixture
def vehicle_client(auth_session):
    client = VehicleApiClient(auth_session)
    return TestScenarios(client)

@pytest.fixture()
def rndm_vehicle_id(auth_session):
    response = auth_session.get(f"{Endpoint.BASE_URL.value}/stock")
    assert response.status_code == 200, "Ошибка авторизации, статус код не 200"

    get_booking = response.json()
    id = random.choice(get_booking)["id"]
    return id

class TestVehicles():

    def test_vehicle_creation(self, vehicle_client):
        data = Generators.generate_vehicle_data(1)[0]
        vehicle_client.creation_vehicle_and_delete(data)


    def test_vehicle_creation_bad_request(self, vehicle_client):
        vehicle_client.error_creation_vehicle(Generators.generate_vehicle_data(1)[0])


    def test_vehicles_exists(self, vehicle_client):
        vehicle_client.get_and_verify_stocks_exist()


    def test_announcements_exists(self, vehicle_client):
        vehicle_client.get_and_verify_ads_exist()


    def test_new_ads_exists(self, vehicle_client):
        data = Generators.generate_vehicle_data(1)[0]
        vehicle_client.creation_ads_announcement(data)

