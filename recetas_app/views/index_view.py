from django.shortcuts import render


def index_view(request):
    context = {}
    response = render(request, 'recetas_app/index.html', context)
    return response
