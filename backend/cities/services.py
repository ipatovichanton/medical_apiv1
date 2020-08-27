from cities_light.models import Region, Country, City


def get_countries():
    return Country.objects.all()


def get_regions():
    return Region.objects.all()


def get_regions_by_country_id(country_id):
    return Region.objects.filter(country_id=country_id)


def get_cities():
    return City.objects.all()


def get_cities_by_region_id(region_id):
    return City.objects.filter(region_id=region_id)