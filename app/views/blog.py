from django.http import Http404
from django.shortcuts import render

from app.middleware import calcular_tiempo_total
from app.middleware import medir
from app.models.Entry import Entry
from app.models.Tipo import Tipo


def blog_index(request):
    medir(request, 'vista_inicio')
    primero = Entry.ultimo()
    context = obtener_context(primero)
    agregar_links(context)
    medir(request, 'vista_final')
    response = render(request, 'app/blog.html', context)
    response['tiempo'] = str(calcular_tiempo_total(request))
    return response


def blog_page(request, slug):
    try:
        primero = Entry.objects.get(handle=slug)
    except Entry.DoesNotExist:
        raise Http404("No existe entrada de blog")
    context = obtener_context(primero)
    agregar_links(context)
    response = render(request, 'app/blog.html', context)
    return response


def agregar_links(context):
    link_list = []
    links = Entry.objects.filter(tipo__idtipo=Tipo.LINK).order_by('-identry')[:10]
    for link in links:
        link_list.append({'handle': link.handle, 'titulo': link.titulo})
        context['links'] = {'cantidad': 10, 'links': link_list}


def obtener_context(entry):
    if entry is not None:
        context = {'entry': entry, 'anterior': Entry.anterior(entry), 'siguiente': Entry.siguiente(entry)}
    else:
        context = {}
    return context
