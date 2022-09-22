from django.shortcuts import render

from recetas.models.receta import Receta


def index_view(request):
    random = Receta.obtener_random()
    context = {'cantidad': Receta.objects.count(), 'visibles': Receta.objects.filter(visible=1).count(), 'random': random}
    response = render(request, 'recetas/index.html', context)
    return response
