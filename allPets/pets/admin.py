
from django.contrib import admin
from .models import (MyPets,Likes,Posts)


# Register your models here.

admin.site.register(MyPets)

admin.site.register(Likes)
admin.site.register(Posts)
