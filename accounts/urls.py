from django.urls import path
from .views import home,CreateCustomer,product,CreateOrder,customer_orders,delete_order,CreateProduct,delete_customer,delete_product


urlpatterns = [
  path('',home,name='home'),
  path('products/',product,name='products'),
  path('create-customer/',CreateCustomer.as_view(),name='create-customer'),
  path('create-order/',CreateOrder.as_view(),name='create-order'),
  path('customer/<int:customer_id>/orders/', customer_orders, name='customer_orders'),
  path('orders/delete/<int:order_id>/', delete_order, name='delete_order'),
  path('products-create',CreateProduct.as_view(),name = 'create-product'),
  path('customers/delete/<int:customer_id>/', delete_customer, name='delete_customer'),
  path('products/delete/<int:product_id>/',delete_product,name='delete-product')

]