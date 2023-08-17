from django.contrib import admin
from recetas.models import Categoria


class CategoriaAdmin(admin.ModelAdmin):
    app_label: 'radmin'


admin.site.register(Categoria, CategoriaAdmin)
