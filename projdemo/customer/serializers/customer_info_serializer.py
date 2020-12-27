from customer.models.customer_info import CustomerInfo
from rest_framework import serializers


class CustomerInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerInfo
        fields = ['id', 'first_name', 'last_name', 'email', 'dob', 'gender', 'extra']