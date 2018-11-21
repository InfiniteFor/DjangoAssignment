from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from localflavor.nl.models import NLZipCodeField

class Details(models.Model):
    FirstName   = models.CharField(max_length=50)
    LastName    = models.CharField(max_length=50)
    PhoneNumber = PhoneNumberField()
    Email       = models.EmailField(max_length=50)
    PostalCode  = NLZipCodeField()
    City        = models.CharField(max_length=50)
    Street      = models.CharField(max_length=50)
    HouseNumber = models.CharField(max_length=10)