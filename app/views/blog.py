from django.shortcuts import render

from app.models.entry import Entry


def blog_index(request):
    primero = Entry.ultimo()
    context = obtener_context(primero)
    response = render(request, 'app/blog.html', context)
    return response


def blog_page(request, slug):
    primero = Entry.obtener_slug(slug)
    context = obtener_context(primero)
    response = render(request, 'app/blog.html', context)
    return response


def obtener_context(entry):
    if entry is not None:
        context = {'entry': entry}
    else:
        context = {}
    context['anterior'] = Entry.anterior(entry)
    context['siguiente'] = Entry.siguiente(entry)
    return context
