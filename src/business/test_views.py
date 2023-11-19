from .models import Business  # Import your Business model
from django.test import RequestFactory
from .views import search, emp
from django.urls import reverse
from django.test import TestCase
from .factories import BusinessFactory


class SearchViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        business = BusinessFactory.create()
        business.name = "Sample Business 1"
        Business.objects.create(
            name="Sample Business 1",  
            NumberofEmployees = business.NumberofEmployees
            )
        business.name = "Another Business"
        Business.objects.create(
            name="Another Business",
            NumberofEmployees = business.NumberofEmployees
            )

    def test_search_with_query(self):
        query = 'Sample'
        url = reverse('search')
        request = self.factory.get(url, {'query': query})
        response = search(request)
        
        self.assertEqual(response.status_code, 200)
        self.assertIn('Sample Business 1', response.content.decode('utf-8'))
        self.assertNotIn('Another Business', response.content.decode('utf-8'))

    def test_search_without_query(self):
        url = reverse('search')
        request = self.factory.get(url)
        response = search(request)
        
        self.assertEqual(response.status_code, 200)
        self.assertIn('Sample Business 1', response.content.decode('utf-8'))
        self.assertIn('Another Business', response.content.decode('utf-8'))

#destroy view
class DestroyViewTest(TestCase):
    def setUp(self):
        self.business = Business.objects.create(name="Test Business", NumberofEmployees = 15)
        self.url = reverse('business_delete', kwargs={'id': self.business.id})

    def test_destroy(self):
        response = self.client.delete(self.url) 
        
        self.assertRedirects(response, '/show')
        
        self.assertFalse(Business.objects.filter(id=self.business.id).exists())
    
#Update View
class UpdateViewTest(TestCase):
    def setUp(self):
        self.business = Business.objects.create(name="Test Business", email="test@example.com", NumberofEmployees = 15)
        self.url = reverse('business_update', kwargs={'id': self.business.id})
        self.updated_data = {
            'name': 'Updated Business',
            'email': 'updated@example.com',
            'NumberofEmployees': 15,
            'ownername': 'Updated Owner',
            'address': 'Updated address',
            'contact': 'Updated contact',
        }

    def test_update_valid_form(self):
        response = self.client.post(self.url, self.updated_data)
        updated_business = Business.objects.get(id=self.business.id)
        self.assertRedirects(response, '/show')
        
        self.assertEqual(updated_business.name, 'Updated Business')
        self.assertEqual(updated_business.email, 'updated@example.com')
        
    def test_update_invalid_form(self):
        invalid_data = {}  # Add incomplete or invalid data
        response = self.client.post(self.url, invalid_data)
        self.assertEqual(response.status_code, 200)

#Create View

class EmpViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_emp_post_valid_form(self):
        business_data = BusinessFactory.stub()
        form_data = {
            'name': business_data.name,
            'email': business_data.email,
            'contact': business_data.contact,
            'address': business_data.address,
            'ownername': business_data.ownername,
            'NumberofEmployees': business_data.NumberofEmployees
        }
        url = reverse('business_create')

        request = self.factory.post(url, form_data)
        response = emp(request)
        
        self.assertEqual(response.status_code, 302)

    def test_emp_post_invalid_form(self):
        form_data = {}
        url = reverse('business_create')

        request = self.factory.post(url, form_data)
        response = emp(request)

        self.assertEqual(response.status_code, 200)

    def test_emp_get(self):
        url = reverse('business_create')

        request = self.factory.get(url)
        response = emp(request)

        self.assertEqual(response.status_code, 200) 
