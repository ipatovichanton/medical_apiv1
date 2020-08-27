from rest_framework import serializers
from .models import Request


class CreateRequestSerializer(serializers.Serializer):
    to_clinic_id = serializers.IntegerField()
    information = serializers.CharField()


class GetRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = "__all__"


class ChangeRequestStatusSerializer(serializers.Serializer):
    status = serializers.ChoiceField(choices=Request.STATUSES)
    answer = serializers.CharField(required=False)