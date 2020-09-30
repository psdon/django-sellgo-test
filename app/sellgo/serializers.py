import os

from django.core.exceptions import ValidationError
from rest_framework import serializers

from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class CreateCsvProductSerializer(serializers.Serializer):
    customer_id = serializers.IntegerField()
    csv = serializers.FileField(write_only=True)

    def validate_csv(self, value):
        ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
        valid_extensions = [
            ".csv",
        ]
        if not ext.lower() in valid_extensions:
            raise ValidationError("Unsupported file extension.")


class CsvProductSerializer(serializers.Serializer):
    customer_id = serializers.IntegerField()
    customer_name = serializers.CharField()

    product_id = serializers.IntegerField()
    product_title = serializers.CharField()
    product_price = serializers.DecimalField(max_digits=10, decimal_places=2)

    last_uploaded = serializers.DateTimeField()
