from django.contrib import admin
from recetas_app.models.insumo import Insumo


class InsumoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoriainsumo')
    list_per_page = 100
    ordering = ('nombre',)


admin.site.register(Insumo, InsumoAdmin)
