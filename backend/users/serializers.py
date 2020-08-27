from rest_framework import serializers
from clinics.models import Clinic
from .models import (
    Ailing,
    Doctor
) 

class UploadPhotoSerializer(serializers.Serializer):
    photo = serializers.ImageField()


class CreateBaseUserSerializer(serializers.Serializer):
    password = serializers.CharField(
        style={"input_type": "password"},
        write_only=True
    )
    passport_id = serializers.CharField()
    passport_series = serializers.CharField()
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    patronymic = serializers.CharField()
    birthday = serializers.DateField()


class CreateDoctorSerializer(CreateBaseUserSerializer):
    about_me = serializers.CharField()
    workplace_id = serializers.IntegerField()
    position = serializers.CharField()


class GetDoctorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"



class CreateAilingSerializer(CreateBaseUserSerializer):
    city_id = serializers.IntegerField()
    address = serializers.CharField()


class GetAilingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ailing
        fields = "__all__"

