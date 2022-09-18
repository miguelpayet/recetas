from django.contrib import admin
from recetas_app.models.tipo import Tipo


class TipoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    list_per_page = 100
    ordering = ('nombre',)


admin.site.register(Tipo, TipoAdmin)
