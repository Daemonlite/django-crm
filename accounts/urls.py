from django.urls import path
from .views import home,CreateCustomer,product,CreateOrder,customer_orders,delete_order

urlpatterns = [
  path('',home,name='home'),
  path('products/',product,name='products'),
  path('create-customer/',CreateCustomer.as_view(),name='create-customer'),
  path('create-order/',CreateOrder.as_view(),name='create-order'),
  path('customer/<int:customer_id>/orders/', customer_orders, name='customer_orders'),
  path('orders/delete/<int:order_id>/', delete_order, name='delete_order')

]