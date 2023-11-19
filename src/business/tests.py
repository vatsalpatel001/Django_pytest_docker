import pytest
from django.urls import reverse
from .factories import BusinessFactory


@pytest.mark.django_db
def test_create_business(client):
    business = BusinessFactory.create()
    data = {
        'name': business.name,
        'email': business.email,
        'contact': business.contact,
        'address': business.address,
        'ownername': business.ownername,
        'NumberofEmployees': business.NumberofEmployees
    }
    response = client.post(reverse('business_create'), data)
    assert response.status_code == 302
    
@pytest.mark.django_db
def test_update_business(client):
    business = BusinessFactory.create()
    new_data = BusinessFactory.stub()
    data = {
        'name': new_data.name,
        'email': new_data.email,
        'contact': new_data.contact,
        'address': new_data.address,
        'ownername': new_data.ownername,
        'NumberofEmployees': new_data.NumberofEmployees
    }
    response = client.post(reverse('business_update', kwargs={'id': business.pk}), data )
    assert response.status_code == 302

@pytest.mark.django_db
def test_delete_business(client):
    business = BusinessFactory.create()
    response = client.post(reverse('business_delete', kwargs={'id': business.pk}))
    assert response.status_code == 302