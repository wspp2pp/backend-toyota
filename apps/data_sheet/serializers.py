from rest_framework import serializers
from .models import DataSheet


class DataSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSheet
        fields = '__all__'
