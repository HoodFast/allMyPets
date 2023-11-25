from django.contrib import admin
from .models import CastomUser
# Register your models here.

class CastomUserAdmin(admin.ModelAdmin):
    pass

admin.site.register(CastomUser,CastomUserAdmin)