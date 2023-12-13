from rest_framework import serializers
from .models import (CastomUser, Profile)
from phonenumber_field.serializerfields import PhoneNumberField


class UsersSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=CastomUser
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    phone_number = PhoneNumberField(region="RU")
    class Meta:
        model=Profile
        fields = '__all__'
