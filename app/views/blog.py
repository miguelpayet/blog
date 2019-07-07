from django.shortcuts import render

from app.models.Entry import Entry
from app.models.Tipo import Tipo


def blog_index(request):
    primero = Entry.ultimo()
    context = obtener_context(primero)
    agregar_links(context)
    response = render(request, 'app/blog.html', context)
    return response


def blog_page(request, slug):
    primero = Entry.obtener_slug(slug)
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
        context = {'entry': entry}
    else:
        context = {}
    context['anterior'] = Entry.anterior(entry)
    context['siguiente'] = Entry.siguiente(entry)
    return context
