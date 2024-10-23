from django.db import models

class Tenant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
   

    def __str__(self):
        return self.name
