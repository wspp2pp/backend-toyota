from pytest import fixture, mark
from rest_framework.test import APIClient
from rest_framework import status
from django.shortcuts import reverse
from .models import Category, Product


@fixture
def create_category():
    return Category.objects.create(name='Test Category')


@fixture
def create_products(create_category):
    category = create_category
    product1 = Product.objects.create(name='Product 1', price=100, year=2022, category=category)
    product2 = Product.objects.create(name='Product 2', price=200, year=2023, category=category)
    return [product1, product2]


@mark.django_db
def test_list_product_by_category(create_products):
    client = APIClient()
    category_id = create_products[0].category_id
    response = client.get(reverse('product:list_product_by_category', args=[category_id]))
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2
    assert response.data[0]['name'] == create_products[0].name
    assert response.data[1]['name'] == create_products[1].name


@mark.django_db
def test_list_product_by_category_no_category_id(create_products):
    client = APIClient()
    response = client.get(reverse('product:list_product_by_category', args=[999]))
    assert response.status_code == status.HTTP_404_NOT_FOUND


@mark.django_db
def test_list_product_by_category_invalid_category_id(create_products):
    client = APIClient()
    response = client.get(reverse('product:list_product_by_category', args=['invalid_id']))
    assert response.status_code == status.HTTP_400_BAD_REQUEST
