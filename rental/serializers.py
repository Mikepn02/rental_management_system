from rest_framework import serializers;
from .models import Property , Tenant , LeaseAgreement


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model= Property
        fields= '__all__'


class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = '__all__'

class LeaseAgreementSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaseAgreement
        fields = '__all__'