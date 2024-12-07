from django import forms
from .models import Property

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['property_name', 'address', 'owner', 'property_type', 'rent_amount', 'monthly_expenses', 'status']


