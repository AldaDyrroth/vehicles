from src.api.constant import Par
from src.data_models.models import VehicleData, VehicleStock, VehicleAds
from src.utils.validator import validate_response
from tenacity import retry, stop_after_delay


class VehicleApiClient:

    def __init__(self, auth_session):
        self.auth_session = auth_session
        self.base_url = Par.BASE_URL.value  # Можно также передавать в конструктор, если он может меняться

    def create_vehicle(self, vehicle_data):
        vehicle_data = vehicle_data
        create = self.auth_session.post(f"{Par.BASE_URL.value}:3002/stock", json=vehicle_data)
        announcement_data = {"id": create.json()["id"], "createdAt": create.json()["createdAt"]}
        validate_response(create, expected_status=201, model=VehicleData, validate_expected_data=False,
                          expected_data=vehicle_data.update(announcement_data))
        return create.json()

    def create_vehicle_noval(self, status: int, vehicle_data):
        vehicle_data = vehicle_data
        create = self.auth_session.post(f"{Par.BASE_URL.value}:3002/stock", json=vehicle_data)
        # announcement_data = {"id": create.json()["id"], "createdAt": create.json()["createdAt"]}
        # validate_response(create, expected_status=404, model=VehicleData, validate_expected_data=False,
        #                   expected_data=vehicle_data.update(announcement_data))
        assert create.status_code == status, f'Status-code {status}'
        return create.json()

    def get_stock(self):
        response = self.auth_session.get(f"{Par.BASE_URL.value}:{Par.STOCK_PORT.value}/stock")
        # validate_response(response, model=VehicleStock, validate_expected_data=False)
        return response.json()

    def get_stock_id(self, vehicle_id):
        response = self.auth_session.get(f"{Par.BASE_URL.value}:{Par.STOCK_PORT.value}/stock")
        # validate_response(response[0], model=VehicleStock)
        assert response.status_code == 200, f'Expected status 200, got {response.status_code}: {response.text}'
        data = response.json()
        for i in range(len(data)):
            if data[i]["id"] == vehicle_id:
                result = data[i]
                break

        return result

    def get_ads(self):
        response = self.auth_session.get(f"{Par.BASE_URL.value}:{Par.ADS_PORT.value}/ads")
        # validate_response(response, model=VehicleAds)
        return response.json()

    def get_ads_id(self, vehicle_id):
        response = self.auth_session.get(f"{Par.BASE_URL.value}:{Par.ADS_PORT.value}/ads")
        # validate_response(response, model=VehicleAds)
        assert response.status_code == 200, f'Expected status 200, got {response.status_code}: {response.text}'
        result = {}
        data = response.json()
        for i in range(len(data)):
            if data[i]["_id"] == vehicle_id:
                result = data[i]
                break

        return result

