from django.http import Http404

from app.models import Coleccion
from .MyViewBase import MyViewBase


class GaleriaView(MyViewBase):
    template_name = 'app/galeria.html'

    def get_context_data(self, **kwargs):
        if 'nombre' in kwargs:
            nombre = kwargs['nombre']
        else:
            raise Http404("No sabemos a qué galería ir")
        try:
            coleccion = Coleccion.objects.get(handle=nombre)
        except Coleccion.DoesNotExist:
            raise Http404("No existe galería %s" % nombre)
        fotos = []
        for foto in coleccion.foto_set.all():
            fotos.append({'url': foto.archivo.url, 'height': foto.archivo.height, 'width': foto.archivo.width})
        contexto = {'fotos': fotos}
        return contexto
