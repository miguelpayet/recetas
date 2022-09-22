from django.contrib import admin
from recetas.models.dificultad import Dificultad


class DificultadAdmin(admin.ModelAdmin):
    pass


admin.site.register(Dificultad, DificultadAdmin)
