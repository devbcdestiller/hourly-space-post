import requests

NASA_URL = 'https://api.nasa.gov'

class APOD:
    def __init__(self, api_key, return_count=1):
        self.api_key = api_key
        self.return_count = return_count
        self.base_path = '/planetary/apod'

    def get(self):
        request_url = f'{NASA_URL}{self.base_path}?count={self.return_count}&api_key={self.api_key}'
        print(request_url)
        response = requests.get(request_url)

        return response.json()
