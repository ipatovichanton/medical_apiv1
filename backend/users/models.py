from cities_light.models import City
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from clinics.models import Clinic
from records.models import MedicalCard
from .managers import UserManager
from .utils import get_user_photo_path
from .validations import PassportIdValidator, validate_birthday


class BaseUser(AbstractBaseUser, PermissionsMixin):
    passport_id_validator = PassportIdValidator()
    passport_id = models.CharField(
        db_index=True,
        max_length=20,
        unique=True,
        validators=[passport_id_validator],
        error_messages={
            "unique": "A user with that passport id already exist"
        }
    )
    photo = models.ImageField(
        upload_to=get_user_photo_path,
        null=True,
        blank=True
    )
    email = models.EmailField(
        db_index=True,
        unique=True
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    passport_series = models.CharField(max_length=10)
    birthday = models.DateField()
    phone = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    archived = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = "passport_id"
    REQUIRED_FIELDS = [
        "email",
        "passport_series",
        "first_name",
        "last_name",
        "patronymic",
        "birthday"
    ]

    def __str__(self):
        return self.passport_id

    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        return '{} {} {}'.format(self.first_name, self.last_name, self.patronymic)



class Doctor(BaseUser):
    position = models.CharField(max_length=100)
    workplace = models.ForeignKey(
        to=Clinic,
        on_delete=models.CASCADE,
        related_name="doctors",
        null=True,
    )
    about_me = models.TextField()


class Ailing(BaseUser):
    city = models.ForeignKey(
        to=City,
        on_delete=models.SET_NULL,
        related_name='ailings',
        null=True
    )
    address = models.CharField(max_length=200)


@receiver(post_save, sender=Ailing)
def create_medical_card(sender, instance, created, **kwargs):
    if created:
        instance.card = MedicalCard.objects.create(user=instance)
        instance.card.save()