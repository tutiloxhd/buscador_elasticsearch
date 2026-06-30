from elastic.client import get_client
from config import INDEX_NAME

es = get_client()


def buscar(terminos: list[str], size: int = 20):

    consulta = {
        "bool": {
            "should": [
                {
                    "match": {
                        "texto": termino
                    }
                }
                for termino in terminos
            ]
        }
    }

    resultado = es.search(
        index=INDEX_NAME,
        query=consulta,
        size=size
    )

    documentos = []

    for hit in resultado["hits"]["hits"]:

        documentos.append({
            "score": hit["_score"],
            **hit["_source"]
        })

    return {
        "total": resultado["hits"]["total"]["value"],
        "documentos": documentos
    }