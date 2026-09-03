import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})

    def get(self, endpoint, params=None):
        response = self.session.get(f"{self.base_url}{endpoint}", params=params)
        return response

    def post(self, endpoint, payload=None):
        response = self.session.post(f"{self.base_url}{endpoint}", json=payload)
        return response