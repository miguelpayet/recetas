from django.contrib import admin
from recetas_app.models.categoriainsumo import CategoriaInsumo


class CategoriaInsumoAdmin(admin.ModelAdmin):
    pass


admin.site.register(CategoriaInsumo, CategoriaInsumoAdmin)
