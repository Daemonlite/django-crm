from django.urls import path
from .views import home,customers,CreateCustomer,product

urlpatterns = [
  path('',home,name='home'),
  path('customers/',customers,name='customer'),
  path('products/',product,name='products'),
  path('create-customer/',CreateCustomer.as_view(),name='create-customer')
]