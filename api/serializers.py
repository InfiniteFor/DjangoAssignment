from customers.models import Customer
from shipping.models import Details
from rest_framework import serializers

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ('FirstName', 'LastName', 'PhoneNumber', 'Email','BirthDate')

class ShippingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Details
        fields = ('FirstName', 'LastName', 'Email','PhoneNumber','City','Street','HouseNumber')