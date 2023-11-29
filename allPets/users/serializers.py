from rest_framework import serializers
from .models import (CastomUser)



class UsersSerializer(serializers.ModelSerializer):
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username',instance.username)
        instance.password = validated_data.get('password',instance.password)
        instance.email = validated_data.get('email',instance.email)
        instance.save()
        return instance
    class Meta:
        model=CastomUser
        fields = '__all__'