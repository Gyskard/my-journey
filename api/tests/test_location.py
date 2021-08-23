import inspect
import os
import sys

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.insert(0, current_dir + "/..")

from fastapi.testclient import TestClient  # noqa: E402
from main import app  # noqa: E402

client = TestClient(app)


def create_location_201():
    response = client.put(
        "/location",
        json={
            "house_number_street": 25,
            "street_name": "Rue de la fontaine triste",
            "city": "Grenoble",
            "county": "France",
            "postal_code": "38000"
        }
    )
    assert response.status_code == 201


def create_location_400():
    response = client.put(
        "/location",
        json={
            "house_number_street": 25,
            "street_name": "Rue de la fontaine triste",
            "city": "Grenoble",
            "county": "France",
            "postal_code": "38000"
        }
    )
    assert response.status_code == 400
    assert response.json() == {'detail': 'Location already exists'}


def get_location_200():
    response = client.get(
        "/location",
        json={
            "house_number_street": 25,
            "street_name": "Rue de la fontaine triste",
            "city": "Grenoble",
            "county": "France",
            "postal_code": "38000"
        }
    )
    assert response.status_code == 200


def get_location_404():
    response = client.get(
        "/location",
        json={
            "house_number_street": 26,
            "street_name": "Rue de la fontaine triste",
            "city": "Grenoble",
            "county": "France",
            "postal_code": "38000"
        }
    )
    assert response.status_code == 404


create_location_201()
create_location_400()
get_location_200()
get_location_404()
