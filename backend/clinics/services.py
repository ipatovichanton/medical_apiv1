from cities_light.models import City
from .models import Clinic


def create_clinic(
    title,
    address,
    city_id,
):
    return Clinic.objects.create(
        title=title,
        address=address,
        city_id=city_id
    )


def get_clinics():
    return Clinic.objects.all()


def get_clinics_by_city(city_id):
    return Clinic.objects.filter(city_id=city_id)
