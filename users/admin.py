from django.contrib import admin
from django import forms

from .models import User


class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(),
        }


class UserModelAdmin(admin.ModelAdmin):
    form = UserModelForm


admin.site.register(User, UserModelAdmin)
