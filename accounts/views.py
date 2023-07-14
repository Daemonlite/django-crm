from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from .models import *
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

def customers(request):
    return render(request,'accounts/customer.html')


class CreateCustomer(CreateView):
    model = Customer
    fields = ['name', 'phone', 'email']
    success_url = reverse_lazy('customer')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateCustomer, self).form_valid(form)
    
class CreateOrder(CreateView):
    model = Order
    fields = '__all__'
    success_url = reverse_lazy('customer')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateOrder, self).form_valid(form)
    

def customer_orders(request, customer_id):
    orders = Order.objects.filter(customer_id=customer_id)
    context = {'orders': orders}
    return render(request, 'accounts/customer.html', context)


def delete_order(order_id):
    try:
        order = Order.objects.get(id=order_id)
        order.delete()
        return True
    except ObjectDoesNotExist:
        return False