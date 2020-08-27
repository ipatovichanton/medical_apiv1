from rest_framework import serializers
from .models import MedicalCard


class GetMedicalCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalCard
        fields = [
            'id',
            'created_at'
        ]