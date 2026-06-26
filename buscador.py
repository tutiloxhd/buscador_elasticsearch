from elasticsearch import Elasticsearch
from config import ELASTIC_URL, INDEX


class BuscadorElastic:

    def __init__(self):
        self.es = Elasticsearch(ELASTIC_URL)
        self.index = INDEX

    ###########################################################
    # BÚSQUEDA SIMPLE
    ###########################################################

    def buscar(self, termino):

        resultado = self.es.search(
            index=self.index,
            query={
                "match": {
                    "texto_pdf": termino
                }
            },
            highlight={
                "fields": {
                    "texto_pdf": {}
                }
            }
        )

        return self._procesar_resultados(resultado)

    ###########################################################
    # PROCESAMIENTO INTERNO
    ###########################################################

    def _procesar_resultados(self, resultado):

        hits = resultado["hits"]["hits"]

        resultados_formateados = []

        for hit in hits:

            source = hit["_source"]

            resultado_item = {
                "id": hit["_id"],
                "nombre": source["nombre"],
                "texto": source["texto_pdf"],
                "fragmento": (
                    hit["highlight"]["texto_pdf"][0]
                    if "highlight" in hit
                    else None
                )
            }

            resultados_formateados.append(resultado_item)

        return resultados_formateados