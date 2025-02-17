import pytest
import httpx

from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
def test_add_website(client):

    url = "/api/websites/"
    data = {"url": "https://www.youtube.com/"}

    response = client.post(url, data, format='json')

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["url"] == "https://www.youtube.com/"


@pytest.mark.django_db
def test_get_websites(client):

    url = "/api/websites/"
    data = {"url": "https://www.youtube.com/"}
    client.post(url, data, format='json')

    response = client.get(url) 

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) > 0 