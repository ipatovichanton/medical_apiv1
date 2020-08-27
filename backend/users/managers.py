from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _validate_fields(
        self,
        email,
        first_name,
        last_name, 
        patronymic,
        birthday,
        password, 
        passport_series,
        passport_id,
        **extra_fields
    ):
        
        if not email:
            raise ValueError("The given email must be set")
        if not first_name:
            raise ValueError("The given first name must be set")
        if not last_name:
            raise ValueError("The given lastname must be set")
        if not patronymic:
            raise ValueError("The given patronymic must be set")
        if not birthday:
            raise ValueError("The given birthday must be set")
        if not passport_series:
            raise ValueError("The given passport series must be set")
        if not passport_id:
            raise ValueError("The given passport id must be set")

    def _create_user(
        self,
        email,
        first_name,
        last_name, 
        patronymic,
        birthday,
        password, 
        passport_series,
        passport_id,
        **extra_fields
    ):

        self._validate_fields(
            email,
            first_name,
            last_name, 
            patronymic,
            birthday,
            password, 
            passport_series,
            passport_id,
            **extra_fields
        )
        email = self.normalize_email(email)
        passport_id = self.model.normalize_username(passport_id)
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            patronymic=patronymic,
            birthday=birthday,
            passport_series=passport_series,
            passport_id=passport_id,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(
        self,
        email,
        first_name,
        last_name, 
        patronymic,
        birthday,
        password, 
        passport_series,
        passport_id,
        **extra_fields
    ):

        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(
            email, first_name, last_name, 
            patronymic, birthday, password, 
            passport_series, passport_id, **extra_fields
        )

    def create_superuser(
        self,
        email,
        first_name,
        last_name, 
        patronymic,
        birthday,
        password,
        passport_series,
        passport_id,
        **extra_fields
    ):

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(
            email,
            first_name,
            last_name, 
            patronymic,
            birthday,
            password, 
            passport_series,
            passport_id,
            **extra_fields
        )

