from django.db import models
from django import forms
from phonenumber_field.modelfields import PhoneNumberField


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50, widget=forms.PasswordInput)
    email = models.EmailField(max_length=75)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    first_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75)
    address = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
