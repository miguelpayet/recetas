from django.contrib import admin
from recetas.models import Receta
import nested_admin

from recetas.models import Ingrediente


class IngredienteAdmin(nested_admin.NestedTabularInline):
    extra = 0
    fields = ('insumo', 'medida', 'cantidad', 'indicaciones',)
    model = Ingrediente


class RecetaAdmin(admin.ModelAdmin):
    fields = ('nombre', 'descripcion', 'porciones', 'instrucciones', 'tipo', 'dificultad', 'visible',)
    inlines = [IngredienteAdmin]
    list_display = ('nombre', 'origen', 'prioridad', 'visible')
    list_per_page = 100
    ordering = ('origen', 'prioridad', 'nombre',)
    search_fields = ('nombre',)


admin.site.register(Receta, RecetaAdmin)
