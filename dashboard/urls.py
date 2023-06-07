from django.urls import path
from .views import *



urlpatterns = [
    path('customers/list/', CustomerListView.as_view(), name='customer-list'),
    path('customers/add/', CustomerCreateView.as_view(), name='customer_create'),
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customer_detail'),
    path('customers/<int:pk>/edit/', CustomerUpdateView.as_view(), name='customer_update'),
    path('customers/<int:pk>/delete/', CustomerDeleteView.as_view(), name='customer_delete'),

    path('employee/list/', EmployeeListView.as_view(), name='employee_list'),
]
