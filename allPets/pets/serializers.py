from rest_framework import serializers

from .myUtils import MyPrimaryKeyRelatedField
from .models import (MyPets,Likes)



class LikesSerializer(serializers.ModelSerializer):
    ownerLikes=serializers.SlugRelatedField(slug_field='username',read_only=True)
    class Meta:
        model=Likes
        fields=('ownerLikes',)

class MyPetsListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MyPets
        fields = ('name' , 'owner','id')


class MyPetsDetailSerializer(serializers.ModelSerializer):
    # likes = LikesSerializer(read_only=True, many=True)
    likes = MyPrimaryKeyRelatedField(
        queryset=Likes.objects.all()
    )
    
    class Meta:
        model = MyPets
        fields = '__all__'

       