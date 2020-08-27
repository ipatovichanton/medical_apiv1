from django.shortcuts import get_object_or_404
from .models import Request


def create_request(
    ailing_id,
    to_clinic_id,
    information
):
    return Request.objects.create(
        from_user_id=ailing_id,
        to_clinic_id=to_clinic_id,
        information=information,
    )


def get_all_requests():
    return Request.objects.all()


def get_requests_for_clinic(clinic_id):
    return Request.objects.filter(to_clinic_id=clinic_id)


def change_request_status(request_id, status, answer=None):
    request = get_object_or_404(Request, pk=request_id)
    request.status = status
    if answer:
        request.answer = answer
    request.save()
    return request
    

    