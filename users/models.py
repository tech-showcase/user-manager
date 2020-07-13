from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.hashers import make_password


class Service(models.Model):
    alphanumeric_regex_validator = RegexValidator(regex=r'^[a-zA-Z0-9_]*$',
                                                  message="Field's value must be alphanumeric and underscore only.")

    code = models.CharField(validators=[alphanumeric_regex_validator], max_length=50, unique=True)
    name = models.CharField(max_length=75)
    description = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['code']

    def __str__(self):
        return self.code


class AccessRight(models.Model):
    alphanumeric_regex_validator = RegexValidator(regex=r'^[a-zA-Z0-9_]*$',
                                                  message="Field's value must be alphanumeric and underscore only.")

    code = models.CharField(validators=[alphanumeric_regex_validator], max_length=50, unique=True)
    name = models.CharField(max_length=75)
    description = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['code']

    def __str__(self):
        return self.code


class Role(models.Model):
    alphanumeric_regex_validator = RegexValidator(regex=r'^[a-zA-Z0-9_]*$',
                                                  message="Field's value must be alphanumeric and underscore only.")

    code = models.CharField(validators=[alphanumeric_regex_validator], max_length=50, unique=True)
    name = models.CharField(max_length=75)
    description = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    access_rights = models.ManyToManyField(AccessRight,
                                           blank=True)

    class Meta:
        ordering = ['code']

    def __str__(self):
        return self.code


class PasswordField(models.CharField):
    description = "A field for inputting password securely."

    def pre_save(self, instance, add):
        val = make_password(instance)
        setattr(instance, self.attname, val)
        return val


class User(models.Model):
    alphanumeric_regex_validator = RegexValidator(regex=r'^[a-zA-Z0-9_]*$',
                                                  message="Field's value must be alphanumeric and underscore only.")
    phone_regex_validator = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                           message="Phone number must be entered in the format: '+999999999'."
                                                   "Up to 15 digits allowed.")

    username = models.CharField(validators=[alphanumeric_regex_validator], max_length=50, unique=True)
    password = PasswordField(max_length=100)
    email = models.EmailField(max_length=75, unique=True)
    phone = models.CharField(validators=[phone_regex_validator], max_length=15, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    role = models.ForeignKey(
        Role,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    access_right = models.ManyToManyField(AccessRight,
                                          blank=True)

    class Meta:
        ordering = ['username']

    def __str__(self):
        return self.username


class Info(models.Model):
    user = models.OneToOneField(
        User,
        primary_key=True,
        on_delete=models.CASCADE
    )
    first_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75)
    address = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['user']

    def __str__(self):
        return self.user.username
