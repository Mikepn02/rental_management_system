from django.db import models
from rental.models import Property
from tenant.models import Tenant
from django.utils.translation import gettext_lazy as _

class LeaseAgreement(models.Model):
    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        related_name="lease_agreements",
        verbose_name=_("Property")
    )
    tenant = models.ForeignKey(
        Tenant,
        on_delete=models.CASCADE,
        related_name="lease_agreements",
        verbose_name=_("Tenant")
    )
    start_date = models.DateField(verbose_name=_("Start Date"))
    end_date = models.DateField(verbose_name=_("End Date"))
    monthly_rent = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_("Monthly Rent")
    )
    lease_signed = models.BooleanField(default=False, verbose_name=_("Lease Signed"))
    date_created = models.DateTimeField(auto_now=True, verbose_name=_("Date Created"))
    date_modified = models.DateTimeField(auto_now=True, verbose_name=_("Last Modified"))

    def __str__(self):
        return f'Lease: {self.property} - {self.tenant}'
