from django.db import models
from rental.models import Property
from tenant.models import Tenant

class LeaseAgreement(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    monthly_rent = models.DecimalField(max_digits=10, decimal_places=2)
    lease_signed = models.BooleanField(default=False)

    def __str__(self):
        return f'Lease: {self.property} - {self.tenant}'

