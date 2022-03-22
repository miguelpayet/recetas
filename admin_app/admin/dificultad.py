from django.contrib import admin
from recetas_app.models.dificultad import Dificultad


class DificultadAdmin(admin.ModelAdmin):
    pass


admin.site.register(Dificultad, DificultadAdmin)
