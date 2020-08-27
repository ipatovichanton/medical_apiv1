from cities_light.models import City
from .models import Pharmacy


def create_pharmacy(
    title,
    address,
    city_id,
):
    return Pharmacy.objects.create(
        title=title,
        address=address,
        city_id=city_id
    )


def get_pharmacies():
    return Pharmacy.objects.all()


def get_pharmacies_by_city(city_id):
    return Pharmacy.objects.filter(city_id=city_id)