from django.apps import apps
from django.contrib.auth.hashers import make_password
from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator, RegexValidator
from django.contrib.auth.models import AbstractUser, BaseUserManager

class SubscribersManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, phone_number, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not phone_number:
            raise ValueError("The given username must be set")
        email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        GlobalUserModel = apps.get_model(
            self.model._meta.app_label, self.model._meta.object_name
        )
        phone_number = GlobalUserModel.normalize_username(phone_number)
        user = self.model(username=phone_number, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone_number, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(phone_number, email, password, **extra_fields)

    def create_superuser(self, phone_number, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(phone_number, email, password, **extra_fields)


class Subscribers(AbstractUser):
	phone_number = models.CharField(max_length=10, validators=[MinLengthValidator(1), MaxLengthValidator(10), RegexValidator('^[0-9]+$')])
	balance = models.IntegerField(null=True, validators=[MinLengthValidator(1), MaxLengthValidator(10)])
	card_number = models.IntegerField(null=True, validators=[MinLengthValidator(1), MaxLengthValidator(10)])

	#objects = SubscribersManager()
	
	#USERNAME_FIELD = 'phone_number'
#class SubUsers(models.Model):
#	user = models.OneToOneField(User, on_delete=models.CASCADE)
#	phone_number = models.CharField(max_length=10)
#	phone_number = models.CharField(max_length=10, null=True, validators=[MinLengthValidator(1), MaxLengthValidator(10), RegexValidator('^[0-9]+$')])

	

