from django.shortcuts import render


def galeria(request, nombre=''):
    context = {}
    response = render(request, 'app/galeria.html', context)
    response['nombre'] = nombre
    return response
