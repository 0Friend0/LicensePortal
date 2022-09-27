from rest_framework import serializers
from licenses.models import License, Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class ClientDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
        extra_kwargs = {"name": {"required": False}, 'admin_poc': {"required": False},}

class LicenseSerializer(serializers.ModelSerializer):
    client_name = serializers.ReadOnlyField()
    client_id = serializers.ReadOnlyField()

    class Meta:
        model = License
        fields = ('id', 'name', 'expiration_date', 'client_name', 'client_id')


class LicenseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = License
        fields = '__all__'
        extra_kwargs = {"name": {"required": False}, 'expiration_date': {"required": False},}