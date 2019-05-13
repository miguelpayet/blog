from django.shortcuts import render
from app.models.entry import Entry


def blog_index(request):
    primero = Entry.ultimo()
    if primero is not None:
        context = {'entry': primero}
    else:
        context = {}
    context['anterior'] = Entry.anterior(primero)
    context['siguiente'] = Entry.siguiente(primero)
    response = render(request, 'app/blog.html', context)
    return response


def blog_page(request, slug):
    primero = Entry.obtener_slug(slug)
    if primero is not None:
        context = {'entry': primero}
    else:
        context = {}
    context['anterior'] = Entry.anterior(primero)
    context['siguiente'] = Entry.siguiente(primero)
    response = render(request, 'app/blog.html', context)
    return response
