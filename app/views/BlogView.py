from django.http import Http404

from app.models.Entry import Entry
from app.models.Tipo import Tipo
from .MyViewBase import MyViewBase


class BlogView(MyViewBase):

    def __init__(self, **kwargs):
        self.context = {}
        super().__init__()

    def agregar_links(self):
        link_list = []
        links = Entry.objects.filter(tipo__idtipo=Tipo.LINK).order_by('-identry')[:10]
        for link in links:
            link_list.append({'handle': link.handle, 'titulo': link.titulo})
            self.context['links'] = {'cantidad': 10, 'links': link_list}

    def obtener_context(self, entry):
        if entry is not None:
            self.context = {'entry': entry, 'anterior': Entry.anterior(entry), 'siguiente': Entry.siguiente(entry)}
        return


class BlogIndexView(BlogView):
    template_name = "app/blog.html"

    def get_context_data(self, **kwargs):
        primero = Entry.ultimo()
        self.obtener_context(primero)
        self.agregar_links()
        return self.context


class BlogPageView(BlogView):
    template_name = "app/blog.html"

    def get_context_data(self, **kwargs):
        if 'slug' in kwargs:
            slug = kwargs['slug']
        else:
            raise Http404("No sabemos a qué página ir")
        try:
            primero = Entry.objects.get(handle=slug)
        except Entry.DoesNotExist:
            raise Http404("No existe entrada de blog")
        self.obtener_context(primero)
        self.agregar_links()
        return self.context
