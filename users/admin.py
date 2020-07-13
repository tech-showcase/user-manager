from django.contrib import admin
from django import forms

from .models import User, Role, Info, AccessRight, Service


class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(),
        }


class UserModelAdmin(admin.ModelAdmin):
    list_filter = ('is_active', 'role')
    form = UserModelForm


admin.site.register(User, UserModelAdmin)
admin.site.register(Info)
admin.site.register(Role)
admin.site.register(AccessRight)
admin.site.register(Service)
