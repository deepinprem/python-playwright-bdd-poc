import pytest

def test_get_all_posts(api_client):
    response = api_client.get("/posts")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_single_post_validation(api_client):
    response = api_client.get("/posts/1")
    assert response.status_code == 200
    
    data = response.json()
    assert data["id"] == 1
    assert "title" in data
    assert "body" in data

def test_create_post(api_client):
    payload = {
        "title": "Automated Test Post - PREM IN PYTHON FRAME",
        "body": "Testing service layer with Pytest",
        "userId": 1
    }
    response = api_client.post("/posts", payload=payload)
    assert response.status_code == 201
    assert response.json()["title"] == payload["title"]

@pytest.mark.parametrize("post_id", [9999, "invalid"])
def test_get_nonexistent_post(api_client, post_id):
    response = api_client.get(f"/posts/{post_id}")
    assert response.status_code == 404