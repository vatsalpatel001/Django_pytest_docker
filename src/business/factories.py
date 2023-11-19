from factory import Faker
from factory.django import DjangoModelFactory
from pytest_factoryboy import register
from .models import Business
from factory import fuzzy

class BusinessFactory(DjangoModelFactory):
    class Meta:
        model = Business

    name = Faker('company')
    email = Faker('email')
    contact = fuzzy.FuzzyText(length=10)
    address = Faker('address')
    ownername = Faker('name')
    NumberofEmployees = Faker('random_int', min=1, max=100)

register(BusinessFactory)