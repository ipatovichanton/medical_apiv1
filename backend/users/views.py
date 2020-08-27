from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from . import serializers, services


class UploadPhoto(APIView):
    def patch(self, request):
        serializer = serializers.UploadPhotoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        services.upload_photo(request.user.id, **serializer.validated_data)

        return Response(status=status.HTTP_200_OK)


class CreateDoctorApi(APIView):
    def post(self, request):
        serializer = serializers.CreateDoctorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        services.create_doctor(**serializer.validated_data)

        return Response(status=status.HTTP_201_CREATED)


class GetDoctorsApi(APIView):
    def get(self, request):
        doctors = services.get_doctors()
        serializer = serializers.GetDoctorsSerializer(doctors, many=True)

        return Response(serializer.data)


class CreateAilingApi(APIView):
    def post(self, request):
        serializer = serializers.CreateAilingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        services.create_ailing(**serializer.validated_data)

        return Response(status=status.HTTP_201_CREATED)


class GetAilingsApi(APIView):
    def get(self, request):
        ailings = services.get_ailings()
        serializer = serializers.GetAilingsSerializer(ailings, many=True)

        return Response(serializer.data)


class GetMyProfile(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user.ailing
        serializer = serializers.GetAilingsSerializer(user)

        return Response(serializer.data)


class ArchiveAilingApi(APIView):
    def delete(self, request, ailing_id):
        services.archive_ailing(ailing_id)

        return Response(status=status.HTTP_204_NO_CONTENT)


class ArchiveDoctorApi(APIView):
    def delete(self, request, doctor_id):
        services.archive_doctor(doctor_id)

        return Response(status=status.HTTP_204_NO_CONTENT)
