from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers, services


class CreateRequestApi(APIView):
    def post(self, request):
        serializer = serializers.CreateRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        services.create_request(
            request.user.id,
            **serializer.validated_data
        )
        return Response(status=status.HTTP_201_CREATED)


class GetRequestApi(APIView):
    def get(self, request):
        requests = services.get_requests_for_clinic(request.user.doctor.workplace_id)
        serializer = serializers.GetRequestSerializer(requests, many=True)

        return Response(serializer.data)


class ChangeRequestStatusApi(APIView):
    def patch(self, request, request_id):
        serializer = serializers.ChangeRequestStatusSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        services.change_request_status(
            request_id,
            **serializer.validated_data
        )

        return Response(status=status.HTTP_200_OK)

