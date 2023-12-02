
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import MyPets
from .serializers import MyPetsListSerializer, MyPetsDetailSerializer
# Create your views here.


class PetsViewSet(APIView):

    def get(self,request):
        queryset = MyPets.objects.all()
        serializer = MyPetsListSerializer(queryset, many=True)
        return Response(serializer.data)


class PetsDetailView(APIView):
    def get(self, request, pk):
        queryset = MyPets.objects.get(id=pk)
        serializer = MyPetsDetailSerializer(queryset)
        return Response(serializer.data)