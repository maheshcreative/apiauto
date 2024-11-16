#api client base class
import requests

class APIClient:
    BASE_URL = "https://jsonplaceholder.typicode.com"
    @staticmethod
    def get(endpoint):
        url = f"{APIClient.BASE_URL}{endpoint}"
        response = requests.get(url)
        return response
    @staticmethod
    def get(endpoint,data):
        url = f"{APIClient.BASE_URL}{endpoint}"
        response = requests.post(url,json=data)
        return response

