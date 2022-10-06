from django.shortcuts import render


def admin_index(request):
    context = {}
    response = render(request, 'admin/indexrecetas.html', context)
    return response
