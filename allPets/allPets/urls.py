"""
URL configuration for allPets project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path, re_path
from pets.views import PetsViewSet, PetsDetailView
from users.views import ProfileView
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'allPets'

router_v1 = routers.DefaultRouter()
router_v1.register(
    prefix='profile', viewset=ProfileView, basename='profile'
    )
# router_v1.register(
#     prefix='pets', viewset=PetsViewSet, basename='pets'
#     )
# router_v1.register(
#     prefix='users', viewset=UsersWiewSet, basename='users'
#     )

urlpatterns = [
    path('', include(router_v1.urls)),
    path('pets/', PetsViewSet.as_view()),
    path('pets/<int:pk>', PetsDetailView.as_view()),
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.jwt')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
