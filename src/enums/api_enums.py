from enum import Enum

class Endpoint(Enum):
    BASE_IP = "localhost"
    STOCK_PORT = "3002"
    ADS_PORT = "3003"
    BASE_URL = f"http://{BASE_IP}"
    ADS_URL = f"{BASE_IP}:{ADS_PORT}"
    HEADERS = {"Content-Type": "application/json", "Accept": "application/json"}