from app.common import BuscadorSolr

from .MyViewBase import MyViewBase


class BuscarView(MyViewBase):
    template_name = 'app/buscar.html'

    def __init__(self, **kwargs):
        self.post_data = None
        super().__init__()

    def get_context_data(self, **kwargs):
        buscador = BuscadorSolr()
        buscador.campos = 'titulo,handle,score'
        buscador.query_fields = ['titulo', 'handle', 'descripcion', 'tags']
        context = buscador.buscar(self.post_data['texto'])
        return context

    def post(self, request, *args, **kwargs):
        self.post_data = request.POST
        return self.get(request, *args, **kwargs)
