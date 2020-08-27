from rest_framework.response import Response
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from . import serializers, services


class CreateClinicApi(APIView):
    def post(self, request):
        serializer = serializers.CreateClinicSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        services.create_clinic(**serializer.validated_data)

        return Response(status=status.HTTP_201_CREATED)


class GetClinicApi(APIView):
    def get(self, request):
        clinics = services.get_clinics()
        serializer = serializers.GetClinicSerializer(clinics, many=True)

        return Response(serializer.data)


class GetClinicsByCityApi(APIView):
    def get(self, request, city_id):
        clinics = services.get_clinics_by_city(city_id)
        serializer = serializers.GetClinicSerializer(clinics, many=True)

        return Response(serializer.data)
        