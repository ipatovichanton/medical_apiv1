"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from authentication import views as auth_views
from cities import views as cities_views
from clinics import views as clinics_views
from requests import views as requests_views
from users import views as users_views
from pharmacy import views as pharmacy_views


requests_patterns = [
    path('requests/', requests_views.GetRequestApi.as_view()),
    path('requests/create/', requests_views.CreateRequestApi.as_view()),
    path('requests/<int:request_id>/update/', requests_views.ChangeRequestStatusApi.as_view())
]

clinics_patterns = [
    path('clinics/', clinics_views.GetClinicApi.as_view()),
    path('clinics/create', clinics_views.CreateClinicApi.as_view()),
    path('cities/<int:city_id>/clinics/', clinics_views.GetClinicsByCityApi.as_view())
]

cities_patterns = [
    path('countries/', cities_views.GetCountriesApi.as_view()),
    path('countries/<int:country_id/regions/>', cities_views.GetRegionsByCountryApi.as_view()),
    path('regions/<int:region_id>/cities/', cities_views.GetCitiesByRegionApi.as_view()),
    path('regions/', cities_views.GetRegionsApi.as_view()),
    path('cities/', cities_views.GetCitiesApi.as_view()),
]

users_patterns = [
    path('ailings/', users_views.GetAilingsApi.as_view()),
    path('ailings/create/', users_views.CreateAilingApi.as_view()),
    path('ailings/<int:ailing_id>/archive/', users_views.ArchiveAilingApi.as_view()),
    path('doctors/', users_views.GetDoctorsApi.as_view()),
    path('doctors/create/', users_views.CreateDoctorApi.as_view()),
    path('doctors/<int:doctor_id>/archive/', users_views.ArchiveDoctorApi.as_view()),
    path('profile/', users_views.GetMyProfile.as_view())
]

pharmacies_patterns = [
    path('pharmacies/', pharmacy_views.GetPharmacyApi.as_view()),
    path('pharmacies/create', pharmacy_views.CreatePharmacyApi.as_view()),
    path('cities/<int:city_id>/pharmacies/', pharmacy_views.GetPharmaciesByCityApi.as_view())
]

apipatterns = [
    path('', include(users_patterns)),
    path('', include(cities_patterns)),
    path('', include(clinics_patterns)),
    path('', include(requests_patterns)),
    path('', include(pharmacies_patterns)),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include((apipatterns, "api"), namespace="api")),
    path('auth/', auth_views.UserLoginView.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
