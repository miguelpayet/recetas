from django.contrib import admin

from recetas.models import Receta

from recetas.models import Ingrediente


class IngredienteAdmin(admin.TabularInline):
    extra = 0
    fields = ('insumo', 'medida', 'cantidad',)
    readonly_fields = ('insumo', 'medida', 'cantidad',)
    model = Ingrediente


class IngredienteInline(admin.TabularInline):
    autocomplete_fields = ['insumo']
    extra = 1
    fields = ('insumo', 'cantidad', 'medida', 'indicaciones',)
    model = Ingrediente


class RecetaAdmin(admin.ModelAdmin):
    fields = ('nombre', 'descripcion', 'porciones', 'instrucciones', 'tipo', 'dificultad', 'visible',)
    inlines = [IngredienteInline]
    list_display = ('nombre', 'origen', 'prioridad', 'visible')
    list_per_page = 100
    ordering = ('origen', 'prioridad', 'nombre',)
    search_fields = ('nombre',)


admin.site.register(Receta, RecetaAdmin)
