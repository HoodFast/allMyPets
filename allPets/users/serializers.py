from rest_framework import serializers
from .models import (CastomUser)



class UsersSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=CastomUser
        fields = '__all__'