from cities_light.models import City
from rest_framework import serializers
from .models import Pharmacy


class CreatePharmacySerializer(serializers.Serializer):
    title = serializers.CharField()
    address = serializers.CharField()
    city_id = serializers.IntegerField()

    
class GetPharmacySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacy
        fields = "__all__"