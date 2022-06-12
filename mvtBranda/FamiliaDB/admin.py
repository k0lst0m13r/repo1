from django.contrib import admin
from FamiliaDB.models import *

# Register your models here.
class FamiliarAdmin(admin.ModelAdmin):
    list_display = ('parentezco', 'nombre', 'edad', 'nacimiento')
    
class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'especie', 'edad')    

admin.site.register(Familiar, FamiliarAdmin)
admin.site.register(Mascota, MascotaAdmin)