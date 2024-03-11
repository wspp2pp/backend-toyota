from pytest import fixture, mark
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import Product, DataSheet
from ..category.models import Category


@fixture
def client():
    return APIClient()


@fixture
def setup_data():
    category = Category.objects.create(name='Test Category')
    product = Product.objects.create(name='Test Product', price=100, year=2022, category=category)
    DataSheet.objects.create(title='Test DataSheet 1', subtitle='Subtitle 1',
                             description='Description 1', principal=False, product=product)
    DataSheet.objects.create(title='Test DataSheet 2', subtitle='Subtitle 2',
                             description='Description 2', principal=True, product=product)
    return product


@mark.django_db
def test_list_data_sheet_by_product(client, setup_data):
    product = setup_data
    url = reverse('data_sheet:list_data_sheet_by_product', kwargs={'product_id': product.id})
    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2
    assert response.data[0]['title'] == 'Test DataSheet 1'
    assert response.data[1]['title'] == 'Test DataSheet 2'


@mark.django_db
def test_list_data_sheet_by_invalid_product(client):
    url = reverse('data_sheet:list_data_sheet_by_product', kwargs={'product_id': 999})
    response = client.get(url)

    assert response.status_code == status.HTTP_404_NOT_FOUND
