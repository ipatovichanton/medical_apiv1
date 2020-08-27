from django.db import models
from cities_light.models import City


class Clinic(models.Model):
    title = models.CharField(max_length=50)
    city = models.ForeignKey(
        to=City,
        on_delete=models.CASCADE
    )
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.title
