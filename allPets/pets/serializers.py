from rest_framework import serializers
from .models import (MyPets,Likes)



class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Likes
        field=('ownerLikes',)

class MyPetsSerializer(serializers.ModelSerializer):
    likes = serializers.PrimaryKeyRelatedField(
        queryset=Likes.objects.all(), many=True
    )
    class Meta:
        model = MyPets
        fields = '__all__'

       