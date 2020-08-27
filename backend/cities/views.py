from rest_framework.response import Response
from rest_framework.views import APIView
from . import serializers, services


class GetCountriesApi(APIView):
    def get(self, request):
        countries = services.get_countries()
        serializer = serializers.GetCountriesSerializer(countries, many=True)

        return Response(serializer.data)


class GetRegionsByCountryApi(APIView):
    def get(self, request, country_id):
        regions = services.get_regions_by_country_id(country_id=country_id)
        serializer = serializers.GetRegionsSerializer(regions, many=True)

        return Response(serializer.data)


class GetCitiesByRegionApi(APIView):
    def get(self, request, region_id):
        cities = services.get_cities_by_region_id(region_id=region_id)
        serializer = serializers.GetCitiesSerializer(cities, many=True)

        return Response(serializer.data)


class GetCitiesApi(APIView):
    def get(self, request):
        cities = services.get_cities()
        serializer = serializers.GetCitiesSerializer(cities, many=True)

        return Response(serializer.data)


class GetRegionsApi(APIView):
    def get(self, request):
        regions = services.get_regions()
        serializer = serializers.GetRegionsSerializer(regions, many=True)

        return Response(serializer.data)
