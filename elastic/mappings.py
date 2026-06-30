from elastic.client import get_client
from config import INDEX_NAME

es = get_client()

mapping = {
    "mappings": {
        "properties": {
            "id_propiedad": {
                "type": "integer"
            },
            "rol": {
                "type": "keyword"
            },
            "tribunal": {
                "type": "text"
            },
            "cuaderno": {
                "type": "keyword"
            },
            "folio": {
                "type": "keyword"
            },
            "fecha": {
                "type": "date",
                "format": "dd/MM/yyyy"
            },
            "tramite": {
                "type": "text"
            },
            "descripcion": {
                "type": "text"
            },
            "pdf": {
                "type": "keyword"
            },
            "texto": {
                "type": "text"
            }
        }
    }
}


def create_index():

    if not es.indices.exists(index=INDEX_NAME):

        es.indices.create(
            index=INDEX_NAME,
            body=mapping
        )

        print(f"Índice '{INDEX_NAME}' creado.")

    else:

        print(f"Índice '{INDEX_NAME}' ya existe.")