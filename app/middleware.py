import time

NOMBRE_LISTA = 'tiempos'
NOMBRE_TIEMPO = 'tiempo'


class Medir:

    def __init__(self, get_response):
        self.get_response = get_response

    def medir(self, request, nombre):
        if not hasattr(request, NOMBRE_LISTA):
            request.tiempos = []
        request.tiempos.append({'nombre': nombre, NOMBRE_TIEMPO: time.time()})
        response = self.get_response(request)
        return response


class MedirInicio(Medir):

    def __call__(self, request):
        return self.medir(request, 'medir_inicio')


class MedirFin(Medir):

    def __call__(self, request):
        return self.medir(request, 'medir_fin')
