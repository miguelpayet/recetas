from django.shortcuts import render

from recetas.models.receta import Receta


def index(request):
    recetas = Receta.obtener_ultimos()
    context = {'recetas': recetas}
    response = render(request, 'recetas/index.html', context)
    return response
