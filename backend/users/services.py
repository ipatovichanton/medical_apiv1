from django.shortcuts import get_object_or_404
from .models import (
    Ailing,
    Doctor
) 


def create_doctor(
    email,
    first_name,
    last_name,
    patronymic,
    birthday,
    password,
    passport_series,
    passport_id,
    position,
    about_me,
    workplace_id
):

    doctor = Doctor(
        email=email,
        first_name=first_name,
        last_name=last_name,
        patronymic=patronymic,
        passport_series=passport_series,
        passport_id=passport_id,
        birthday=birthday,
        position=position,
        about_me=about_me,
        workplace_id=workplace_id
    )
    doctor.set_password(password)
    doctor.save()
    return doctor


def get_doctors():
    return Doctor.objects.all()

def archive_doctor(doctor_id):
    doctor = get_object_or_404(Doctor, pk=doctor_id)
    doctor.archived = True
    doctor.save()
    return doctor


def create_ailing(
    email,
    first_name,
    last_name,
    patronymic,
    birthday,
    password,
    passport_series,
    passport_id,
    city_id,
    address
):
    ailing = Ailing(
        email=email,
        first_name=first_name,
        last_name=last_name,
        patronymic=patronymic,
        passport_series=passport_series,
        passport_id=passport_id,
        birthday=birthday,
        city_id=city_id,
        address=address
    )

    ailing.set_password(password)
    ailing.save()
    return ailing


def get_ailings():
    return Ailing.objects.all()


def archive_ailing(ailing_id):
    ailing = get_object_or_404(Ailing, pk=ailing_id)
    ailing.archived = True
    ailing.save()
    return ailing


def upload_photo(user_id):
    pass
