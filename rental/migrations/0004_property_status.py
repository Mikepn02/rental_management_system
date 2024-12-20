# Generated by Django 5.1.2 on 2024-11-24 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0003_property_monthly_expenses'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='status',
            field=models.CharField(choices=[('available', 'Available'), ('rented', 'Rented'), ('pending', 'Pending')], default='available', max_length=20),
        ),
    ]
