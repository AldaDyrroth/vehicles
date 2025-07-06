from src.scenarios.test_scenarios import TestScenarios
from src.api.api_client import VehicleApiClient
from src.data_models.models import Generators
import pytest

@pytest.fixture
def vehicle_client(auth_session):
    client = VehicleApiClient(auth_session)
    return TestScenarios(client)

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

