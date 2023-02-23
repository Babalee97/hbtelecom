from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator, RegexValidator
from django.contrib.auth.models import AbstractUser

class Subscribers(AbstractUser):
    phone_number = models.CharField(max_length=10, validators=[MinLengthValidator(1), MaxLengthValidator(10), RegexValidator('^[0-9]+$')])