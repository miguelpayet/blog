import json

import requests
from django.conf import settings


class BuscadorSolr:

    def __init__(self):
        self.campos = []
        self.error = ""
        self.query = None
        self.query_fields = ''
        self.response = None
        self.response_json = None
        self.rows = 500
        self.start = 0
        self.texto = ''
        self.tipo_busqueda = 'edismax'

    def buscar(self, texto):
        self.texto = texto
        self.get_query()
        self.consultar()
        return self.validar()

    def consultar(self):
        resp = requests.post(settings.SOLR_URL, data=self.query)
        self.response = json.loads(resp.content)

    def get_query(self):
        solr_dict = {'q': self.texto, 'defType': self.tipo_busqueda, 'qf': self.query_fields, 'fl': self.campos,
                     'start': self.start, 'rows': self.rows, 'wt': 'json'}
        self.query = solr_dict

    def validar(self):
        if 'response' in self.response:
            return self.response['response']
        raise Exception('no hubo respuesta')
