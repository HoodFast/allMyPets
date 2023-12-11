from rest_framework import serializers
from .models import (CastomUser, Profile)



class UsersSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=CastomUser
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Profile
        fields = '__all__'
