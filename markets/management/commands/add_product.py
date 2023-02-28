import csv
from django.core.management.base import BaseCommand
from ...models import Product

class Command(BaseCommand):
    help = 'Displays current time'

    def add_arguments(self, parser):
        parser.add_argument('-p', '--path', type=str, help='path to csv file',)


    def handle(self, *args, **kwargs):
        path = kwargs.get('path')
        file = open(path)
        csvreader = csv.reader(file)
        for row in csvreader:
            Product.objects.create(name=row)


