from customers.models import Customer
from shipping.models import Details
from rest_framework import viewsets
from api.serializers import CustomerSerializer, ShippingSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Customers to be viewed or edited.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ShippingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows SchippingDetails to be viewed or edited.
    """
    queryset = Details.objects.all()
    serializer_class = ShippingSerializer