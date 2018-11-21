from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from customers.views import customerform
from shipping.views import shippingform
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'customer', views.CustomerViewSet)
router.register(r'shipping', views.ShippingViewSet)

urlpatterns = [
    url(r'api/', include(router.urls)),
    url(r'^customer/', customerform),
    url(r'^shipping/', shippingform),
    path('admin/', admin.site.urls),
]
