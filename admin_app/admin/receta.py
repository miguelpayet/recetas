from django.contrib import admin
from recetas_app.models.receta import Receta


class RecetaAdmin(admin.ModelAdmin):
    # list_display = ('nombre', 'categoriainsumo')
    list_per_page = 100
    ordering = ('nombre',)


admin.site.register(Receta, RecetaAdmin)
