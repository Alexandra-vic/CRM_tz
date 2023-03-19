from django.db import models

from django.urls import reverse, reverse_lazy

from markets.models import Location, Product


class Customer(models.Model):
    first_name = models.CharField(
        max_length=100, 
        blank=True, 
        null=True, 
        verbose_name='имя',
    )
    surname = models.CharField(
        max_length=100, 
        blank=True, 
        null=True, 
        verbose_name='фамилия',
    )
    age = models.IntegerField()
    gender = models.CharField(
        max_length=100, 
        blank=True, 
        null=True, 
        verbose_name='пол',
    )
    location = models.ForeignKey(
        Location, 
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.first_name}  {self.surname}'
    
    def get_absolute_url(self):
        return reverse_lazy('customer_detail', args=[str(self.id)])
    
    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        ordering = ['-id']


class Employee(models.Model):
    first_name = models.CharField(
        max_length=100, 
        blank=True, 
        null=True, 
        verbose_name='имя',
    )
    surname = models.CharField(
        max_length=100, 
        blank=True, 
        null=True, 
        verbose_name='фамилия',
    )
    gender = models.CharField(
        max_length=100, 
        blank=True, 
        null=True, 
        verbose_name='пол',
    )
    location = models.ForeignKey(
        Location, 
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.first_name
    
    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
        ordering = ['-id']


class Order(models.Model):
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE, 
        related_name='product', 
        verbose_name='продукт',
    )    
    employee = models.ForeignKey(
        Employee, 
        on_delete=models.CASCADE, 
        related_name='employee', 
        verbose_name='сотрудник',
    )
    customer = models.ForeignKey(
        Customer, 
        on_delete=models.CASCADE, 
        related_name='customer', 
        verbose_name='клиент',
    )
    date = models.DateField(
        auto_now_add=True, 
        null=True, 
        verbose_name='дата заказа',
    )

    def __str__(self):
        return self.product.name
    
    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ['-id']
