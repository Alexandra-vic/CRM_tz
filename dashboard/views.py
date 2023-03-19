from django.shortcuts import render

from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from dashboard.models import Customer, Employee, Order


def index(request):
    return render(request, 'base.html')


class CustomerListView(ListView):
    model = Customer
    template_name = 'customer/customer_list.html'
 
 
class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customer_detail.html'
    slug_field = 'id'
    slug_url_kwarg = 'id'
    success_url = reverse_lazy('customer-list')
    
 
class CustomerCreateView(CreateView):
    model = Customer
    template_name = 'customer/customer_create.html'
    fields = [
        'first_name', 
        'surname', 
        'age',
        'gender',
        'location',
    ]
    success_url = reverse_lazy('customer-list')

    
class CustomerUpdateView(UpdateView):
    model = Customer
    template_name = 'customer_edit.html'
    fields = [
        'first_name', 
        'surname', 
        'age',
        'gender',
        'location',
    ]
 
 
class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customer_delete.html'
    success_url = reverse_lazy('customer_list.html')


class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee/employee_list.html'


class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employee/employee_detail.html'    


class EmployeeCreateView(CreateView):
    model = Employee
    template_name = 'employee/employee_create.html'
    fields = [
        'first_name', 
        'surname', 
        'gender',
        'location',
    ]
    success_url = reverse_lazy('employee_list')


class EmployeeUpdateView(UpdateView):
    model = Employee
    template_name = 'employee/employee_update.html'
    fields = [
        'first_name', 
        'surname', 
        'gender',
        'location',
    ]


class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'employee_delete.html'
    success_url = reverse_lazy('home')    


class OrderListView(ListView):
    model = Order
    template_name = 'base.html'    


class OrderDetailView(DetailView):
    model = Order
    template_name = 'order_detail.html'   


class OrderCreateView(CreateView):
    model = Order
    template_name = 'order_new.html'
    fields = [
        'product',
        'employee',
        'customer',
        'location',
    ]


class EmployeeUpdateView(UpdateView):
    model = Employee
    template_name = 'order_edit.html'
    fields = [
        'product',
        'employee',
        'customer',
        'location',
    ]


class OrderListView(ListView):
    model = Order
    template_name = 'order/orde_list.html'
