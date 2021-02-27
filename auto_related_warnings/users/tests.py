import pytest
from rest_framework.test import APIClient

from .models import User


@pytest.mark.django_db
def test_create_user():
    client = APIClient()

    response = client.post(
        "/users",
        {
            "email": "test@email.com",
            "password": "GoodPassword1!",
            "some_serializer_field": "Serializer value",
        },
    )

    assert response.status_code == 201
    assert response.data["email"] == "test@email.com"


@pytest.mark.django_db
def test_retrieve_user():
    user = User.objects.create(
        email="test@email.com",
        password="GoodPassword1!",
        some_model_field="Model value",
    )

    client = APIClient()

    response = client.get(f"/users/{user.id}")

    assert response.status_code == 200
    assert response.data["email"] == "test@email.com"
