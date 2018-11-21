from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Customer(models.Model):
    FirstName   = models.CharField(max_length=50)
    LastName    = models.CharField(max_length=50)
    PhoneNumber = PhoneNumberField(error_messages = {'invalid': 'Phonenumber must be in following format +999999999.'})
    Email       = models.EmailField(max_length=50, unique=True)
    BirthDate   = models.DateField()



