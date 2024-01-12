from django.contrib import admin
from . import models

# Register your models here.
class PokemonAdmin(admin.ModelAdmin):
    list_display = ["name", "id_region", "id_kind_display"]
    

    def id_kind_display(self, obj):
        return obj.id_kind.name  # Reemplaza 'nombre' con el campo correcto en tu modelo de Tipo
    id_kind_display.short_description = "Tipo"  # Cambia el nombre de la columna en la vista de lista

class KindAdmin(admin.ModelAdmin):
    list_display = ['name_kind']
    
class RegionAdmin(admin.ModelAdmin):
    list_display = ["name_region"]

admin.site.register(models.Pokemon, PokemonAdmin)
admin.site.register(models.Kind, KindAdmin)
admin.site.register(models.Region, RegionAdmin)