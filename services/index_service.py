from elastic.client import get_client
from config import INDEX_NAME
from utils.parser import parse_documentos

es = get_client()


def indexar(json_data):

    documentos = parse_documentos(json_data)

    cantidad = 0

    for doc in documentos:

        es.index(
            index=INDEX_NAME,
            document=doc
        )

        cantidad += 1

    return {

        "status": "ok",

        "documentos_indexados": cantidad

    }