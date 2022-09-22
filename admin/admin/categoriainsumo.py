from django.contrib import admin
from recetas.models import CategoriaInsumo


class CategoriaInsumoAdmin(admin.ModelAdmin):
    pass


admin.site.register(CategoriaInsumo, CategoriaInsumoAdmin)
