from django import forms 
import datetime 
from .models import Details

class ShippingForm(forms.ModelForm):
    class Meta:
        model = Details
        fields = ["FirstName", "LastName", "PhoneNumber", "Email","PostalCode","City","Street","HouseNumber"]