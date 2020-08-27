from django.core import validators
from django.utils.deconstruct import deconstructible
from django.core.exceptions import ValidationError

import datetime


def validate_birthday(birthday):
    if birthday > datetime.date.today():
        raise ValidationError("The birthday can't be in future")


@deconstructible
class PassportIdValidator(validators.RegexValidator):
    message = (
        "Enter a valid passport id. This value may contain only letters, "
        "numbers"
    )