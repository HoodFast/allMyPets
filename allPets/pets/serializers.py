from rest_framework import serializers

from .myUtils import MyPrimaryKeyRelatedField
from .models import (MyPets,Likes,Post)



class LikesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Likes
        fields=('ownerLikes',)

class MyPetsListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MyPets
        fields = ('name' , 'owner','id')


class MyPetsDetailSerializer(serializers.ModelSerializer):
    # likes = LikesSerializer(read_only=True, many=True)
    likes = serializers.PrimaryKeyRelatedField(
        queryset=Likes.objects.all()
    )
    # posts = serializers.PrimaryKeyRelatedField(
    #     queryset=Post.objects.all()
    # )
    class Meta:
        model = MyPets
        fields = '__all__'

    def get_likes(self,obj):
        queryset = Likes.objects.filter(id=obj.id)
        
       