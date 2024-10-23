from django.db import models

class Property(models.Model):
    property_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    owner = models.CharField(max_length=100)
    property_type = models.CharField(max_length=50, choices=[('House', 'House'), ('Apartment', 'Apartment')])
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.property_name


