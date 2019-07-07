from django.shortcuts import render

from app.common import BuscadorSolr


def buscar(request):
    if request.method == 'POST':
        post = request.POST
        buscador = BuscadorSolr()
        buscador.campos = 'titulo,handle,score'
        buscador.query_fields = ['titulo', 'handle', 'descripcion', 'tags']
        resp_json = buscador.buscar(post['texto'])
        return render(request, 'app/buscar.html', resp_json)
