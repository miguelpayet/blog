from time import time


def calcular_tiempo_total(request):
    t = request.tiempos[0]
    ti = t['tiempo']
    tf = time()
    tt = tf - ti
    return tt


def medir(request, nombre):
    if not hasattr(request, 'tiempos'):
        request.tiempos = []
    request.tiempos.append({'nombre': nombre, 'tiempo': time()})


class Medir:

    def __init__(self, get_response):
        self.get_response = get_response

    def medir(self, request, nombre):
        medir(request, nombre)
        response = self.get_response(request)
        return response


class MedirInicio(Medir):

    def __call__(self, request):
        return self.medir(request, 'middleware_inicio')


class MedirFin(Medir):

    def __call__(self, request):
        return self.medir(request, 'middleware_fin')
