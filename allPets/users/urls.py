from rest_framework import routers
from django.urls import include, path
from .views import UsersWiewSet


app_name = 'users'

router_v1 = routers.DefaultRouter()

router_v1.register('users', UsersWiewSet)

urlpatterns = [
    path('', include(router_v1.urls)),
    path('auth/', include('rest_framework.urls'))
]