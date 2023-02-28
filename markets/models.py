from django.db import models


class Location(models.Model):
    city = models.CharField(max_length=100, blank=True, null=True, verbose_name='город')

    def __str__(self):
        return self.city
    
    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'


class Product(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name='наименовние')
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=8, decimal_places=0, null=True)


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

