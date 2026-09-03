import pytest
from utils.api_client import APIClient

@pytest.fixture(scope="session")
def api_client():
    base_url = "https://jsonplaceholder.typicode.com"
    return APIClient(base_url)