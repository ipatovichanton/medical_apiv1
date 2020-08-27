 
from rest_framework.response import Response
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from . import serializers, services


class CreatePharmacyApi(APIView):
    def post(self, request):
        serializer = serializers.CreatePharmacySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        services.create_pharmacy(**serializer.validated_data)

        return Response(status=status.HTTP_201_CREATED)


class GetPharmacyApi(APIView):
    def get(self, request):
        pharmacies = services.get_pharmacies()
        serializer = serializers.GetPharmacySerializer(pharmacies, many=True)

        return Response(serializer.data)


class GetPharmaciesByCityApi(APIView):
    def get(self, request, city_id):
        pharmacies = services.get_clinics_by_city(city_id)
        serializer = serializers.GetPharmacySerializer(pharmacies, many=True)

        return Response(serializer.data)