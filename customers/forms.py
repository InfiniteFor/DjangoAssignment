from django import forms 
import datetime 
from customers.models import Customer

class CustomerForm(forms.ModelForm):
    now = datetime.datetime.now()
    BirthDate   = forms.DateField (widget=forms.SelectDateWidget(years=range(now.year-100, now.year)))
    class Meta:
        model = Customer
        fields = ["FirstName", "LastName", "PhoneNumber", "Email","BirthDate"]