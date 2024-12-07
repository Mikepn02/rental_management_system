from django.db import models

class Property(models.Model):
    class PropertyType(models.TextChoices):
        HOUSE = 'House', 'House'
        APARTMENT = 'Apartment', 'Apartment'

    class PropertyStatus(models.TextChoices):
        AVAILABLE = 'available', 'Available'
        RENTED = 'rented', 'Rented'
        PENDING = 'pending', 'Pending'

    property_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    owner = models.CharField(max_length=100)
    property_type = models.CharField(max_length=50, choices=PropertyType.choices)
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)
    monthly_expenses = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(
        max_length=20,
        choices=PropertyStatus.choices,
        default=PropertyStatus.AVAILABLE,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.property_name} - {self.address}"
