from rest_framework import viewsets
from django.shortcuts import render

from pets.models import MyPets
from pets.serializers import MyPetsSerializer
# Create your views here.


class PetsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MyPets.objects.all()
    serializer_class = MyPetsSerializer
