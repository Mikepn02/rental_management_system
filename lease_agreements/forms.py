from django import forms
from .models import LeaseAgreement

class LeaseAgreementForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = LeaseAgreement
        fields = ['property', 'tenant', 'start_date', 'end_date', 'monthly_rent', 'lease_signed']
