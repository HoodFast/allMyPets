from django.contrib import admin
from .models import CastomUser, Profile
from django import forms
from phonenumber_field.formfields import PhoneNumberField
# Register your models here.

admin.site.register(CastomUser)
admin.site.register(Profile)


