from django.forms import ModelForm

from .models import Location, Product


class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = ['city']

form = LocationForm()

location = Location.objects.get(pk=1)
form = LocationForm(instance=location)

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'location']

form = ProductForm()

product = Product.objects.get(pk=1)
form = ProductForm(instance=product)        