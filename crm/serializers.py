from rest_framework import serializers
from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'created_at', 'tc_no', 'first_name', 'last_name',
                  'phone', 'city', 'district']
        