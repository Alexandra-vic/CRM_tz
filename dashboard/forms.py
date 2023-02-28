from django import forms
from .models import Customer, Employee, Order


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = (
            'first_name', 
            'surname', 
            'age', 
            'gender', 
            'location',
        )


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = (
            'first_name',
            'surname',
            'gender',
            'location',
        )


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = (
            'product',
            'employee',
            'customer',
            'location',
        )      