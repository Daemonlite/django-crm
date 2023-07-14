from django.urls import path
from .views import home,customers,CreateCustomer,product,CreateOrder,customer_orders

urlpatterns = [
  path('',home,name='home'),
  path('customers/',customers,name='customer'),
  path('products/',product,name='products'),
  path('create-customer/',CreateCustomer.as_view(),name='create-customer'),
  path('create-order/',CreateOrder.as_view(),name='create-order'),
  path('customer/<int:customer_id>/orders/', customer_orders, name='customer_orders'),
]