from cities_light.models import City
from rest_framework import serializers
from .models import Clinic


class CreateClinicSerializer(serializers.Serializer):
    title = serializers.CharField()
    address = serializers.CharField()
    city_id = serializers.IntegerField()

    
class GetClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = "__all__"