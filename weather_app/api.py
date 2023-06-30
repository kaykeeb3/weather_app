import requests
from models import Clima

class WeatherAPI:
    def __init__(self):
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"
        self.api_key = "sua_api_key"

    def obter_clima(self, cidade):
        params = {
            "q": cidade,
            "appid": self.api_key,
            "units": "metric"
        }

        try:
            response = requests.get(self.base_url, params=params)
            data = response.json()
            clima = Clima(data)
            return clima
        except requests.exceptions.RequestException as e:
            print("Erro na requisição:", e)
            return None
