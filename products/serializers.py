from rest_framework import serializers

from accounts.serializers import AccountSerializer
from .models import Product


class ProductSerializer(serializers.ModelSerializer):

    seller = AccountSerializer(read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "seller",
            "description",
            "price",
            "quantity",
            "is_active",
        ]
        extra_kwargs = {
            "is_active": {"default": True},
            "quantity": {"min_value": 0},
        }


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "description",
            "price",
            "quantity",
            "is_active",
            "seller_id",
        ]
        read_only_fields = [
            "seller_id"
        ]
        extra_kwargs = {
            "is_active": {"default": True}
        }
