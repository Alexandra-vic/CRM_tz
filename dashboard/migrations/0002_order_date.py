# Generated by Django 4.1.7 on 2023-02-27 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
