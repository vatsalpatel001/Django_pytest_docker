from django.db import models

# Create your models here.

class Business(models.Model):  
    name = models.CharField(max_length=100)  
    email = models.EmailField()  
    contact = models.CharField(max_length=15) 
    address = models.CharField(max_length=500)
    ownername = models.CharField(max_length=100)
    NumberofEmployees = models.IntegerField()

    class Meta:  
        db_table = "business"  