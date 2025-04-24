# gestion/serializers.py
from rest_framework import serializers # type: ignore
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'  # Incluye todos los campos del modelo