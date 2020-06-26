from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.hashers import make_password


class PasswordField(models.CharField):
    description = "A field for inputting password securely."

    def pre_save(self, instance, add):
        val = make_password(instance)
        setattr(instance, self.attname, val)
        return val


class User(models.Model):
    username = models.CharField(max_length=50)
    password = PasswordField(max_length=50)
    email = models.EmailField(max_length=75)
    phone_regex_validator = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                           message="Phone number must be entered in the format: '+999999999'."
                                                   "Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex_validator], max_length=15)
    first_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75)
    address = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
