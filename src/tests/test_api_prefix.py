from fastapi.testclient import TestClient


from api.routes.router_with_prefix import router as router_with_prefix
from api.routes.router_without_prefix import router as router_without_prefix


def test_prefix_in_router():
    client = TestClient(router_with_prefix)
    response = client.get("/test")
    assert response.status_code == 200


def test_prefix_in_include_router():
    client = TestClient(router_without_prefix)
    response = client.get("/test")
    assert response.status_code == 200
