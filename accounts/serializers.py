from rest_framework import serializers

from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'username', 'first_name', 'last_name',
                  'is_seller', 'password', 'date_joined', 'is_active', 'is_superuser')
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ('id', 'date_joined', 'is_active', 'is_superuser')

    def create(self, validated_data):
        return Account.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class DeactivateAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = (
            'id', 'username', 'first_name', 'last_name',
                  'is_seller', 'date_joined', 'is_active')
