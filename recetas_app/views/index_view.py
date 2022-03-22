from django.shortcuts import render

from recetas_app.models.receta import Receta


def index_view(request):
    context = {'cantidad': Receta.objects.count(), 'visibles': Receta.objects.filter(visible=1).count()}
    response = render(request, 'recetas_app/index.html', context)
    return response
