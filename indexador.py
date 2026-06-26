import pymysql
from elasticsearch import Elasticsearch

from config import DB_CONFIG, ELASTIC_URL, INDEX


###########################################################
# CONEXIONES
###########################################################

def conectar_db():
    return pymysql.connect(
        **DB_CONFIG,
        cursorclass=pymysql.cursors.DictCursor
    )


def conectar_elastic():
    return Elasticsearch(ELASTIC_URL)


###########################################################
# ELASTICSEARCH
###########################################################

def crear_indice(es):

    if not es.indices.exists(index=INDEX):

        es.indices.create(index=INDEX)

        print(f"Índice '{INDEX}' creado.")


###########################################################
# INDEXACIÓN
###########################################################

def indexar_documentos(es, documentos):

    if not documentos:
        return

    print(f"\nIndexando {len(documentos)} documentos...")

    for doc in documentos:

        es.index(
            index=INDEX,
            id=doc["id"],
            document={
                "id": doc["id"],
                "nombre": doc["nombre"],
                "texto_pdf": doc["texto_pdf"]
            }
        )

    # Hace visibles inmediatamente los documentos
    es.indices.refresh(index=INDEX)

    print("Indexación completada.")