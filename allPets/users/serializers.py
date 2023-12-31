from rest_framework import serializers
from .models import (CastomUser, Profile)
from phonenumber_field.serializerfields import PhoneNumberField
from django.contrib.auth.hashers import make_password

class UsersSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(
    #     max_length=68, min_length=6)
    class Meta:
        model=CastomUser
        fields = '__all__'

    # def validate_password(self, value):
    #     return make_password(value)


class ProfileSerializer(serializers.ModelSerializer):
    phone_number = PhoneNumberField(region="RU")
    class Meta:
        model=Profile
        fields = '__all__'
