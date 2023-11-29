from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import render
from users.models import CastomUser
from users.serializers import UsersSerializer

# Create your views here.
class UsersWiewSet(viewsets.ModelViewSet):
    queryset=CastomUser.objects.all()
    serializer_class=UsersSerializer

    def put(self,request, *args,**kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response ({'error':'error'})
        try:
            instance = CastomUser.objects.get(pk=pk)
        except:
            return Response ({'error':'obj not find'})
        
        serializer = UsersSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response({'post':serializer.data})