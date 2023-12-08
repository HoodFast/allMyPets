
from django.contrib import admin
from .models import (MyPets,Likes,Posts)

# Register your models here.
class MyPetsAdmin(admin.ModelAdmin):
    pass

admin.site.register(MyPets,MyPetsAdmin)

class LikesAdmin(admin.ModelAdmin):
    pass

admin.site.register(Likes,LikesAdmin)
admin.site.register(Posts)