import pytest
from django.urls import reverse
from .models import Category


@pytest.mark.django_db
def test_list_categories(client):
    Category.objects.create(name='Category 1')
    Category.objects.create(name='Category 2')

    url = reverse('category:list_categories')
    response = client.get(url)

    assert response.status_code == 200
    assert len(response.json()['categories']) == 2
    assert response.json()['categories'][0]['name'] == 'Category 1'
    assert response.json()['categories'][1]['name'] == 'Category 2'


@pytest.mark.django_db
def test_list_categories_no_categories(client):
    url = reverse('category:list_categories')
    response = client.get(url)

    assert response.status_code == 404
