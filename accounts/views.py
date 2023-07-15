from django.forms.models import BaseModelForm
from django.shortcuts import render,get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from .models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    context = {'orders':orders,'customers':customers,'total_customers':total_customers,
               'total_orders':total_orders,'delivered':delivered,'pending':pending}
    return render(request,'accounts/dashboard.html',context)

def product(request):
    products = Product.objects.all()

    return render(request,'accounts/products.html',{'products':products})


class CreateProduct(CreateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('products')

    def form_invalid(self, form):
        form.instance.user = self.request.user
        return super(CreateCustomer).form_invalid(form)

class CreateCustomer(CreateView):
    model = Customer
    fields = ['name', 'phone', 'email']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateCustomer, self).form_valid(form)
    
class CreateOrder(CreateView):
    model = Order
    fields = '__all__'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateOrder, self).form_valid(form)
    
def customer_orders(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    orders = Order.objects.filter(customer=customer)
    order_count = orders.count()
    context = {'customer': customer, 'orders': orders, 'order_count': order_count}
    return render(request, 'accounts/customer.html', context)

def delete_order(request, order_id):
    try:
        order = Order.objects.get(id=order_id)
        order.delete()
        return HttpResponseRedirect('/')
    except Order.DoesNotExist:
        return HttpResponse("Order does not exist.")
    
def delete_customer(request, customer_id):
    try:
        customer = Customer.objects.get(id=customer_id)
        customer.delete()
        return  HttpResponseRedirect('/')
    except customer.DoesNotExist:
        return HttpResponse("customer does not exist.")
