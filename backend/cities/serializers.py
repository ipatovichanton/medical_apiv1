from cities_light.models import Region, City, Country
from rest_framework import serializers


class GetCitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"


class GetRegionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = "__all__"


class GetCountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all___"