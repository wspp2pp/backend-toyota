import pytest
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import Info


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def setup_data():
    Info.objects.create(name='Info 1', url='https://example.com', section=1)
    Info.objects.create(name='Info 2', url='https://example.org', section=2)


@pytest.mark.django_db
def test_list_info(client, setup_data):
    url = reverse('info:list_info')
    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data['info']) == 2
    assert response.data['info'][0]['name'] == 'Info 1'
    assert response.data['info'][0]['url'] == 'https://example.com'
    assert response.data['info'][0]['section'] == 1
    assert response.data['info'][1]['name'] == 'Info 2'
    assert response.data['info'][1]['url'] == 'https://example.org'
    assert response.data['info'][1]['section'] == 2


@pytest.mark.django_db
def test_list_info_no_info(client):
    url = reverse('info:list_info')
    response = client.get(url)

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.data['error'] == 'No info found'
