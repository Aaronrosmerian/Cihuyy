# prediksi/serializers.py
from rest_framework import serializers
from .models import PermintaanIkan

class PermintaanIkanSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermintaanIkan
        fields = '__all__'
