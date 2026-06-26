import time

from indexador import conectar_db, conectar_elastic, crear_indice, indexar_documentos
from config import INDEX

INTERVALO = 5


###########################################################
# COLA
###########################################################

def obtener_queue(cursor):

    cursor.execute("""
        SELECT id, document_id
        FROM index_queue
        ORDER BY id
    """)

    return cursor.fetchall()


###########################################################
# DOCUMENTOS
###########################################################

def obtener_documentos(cursor, ids):

    if not ids:
        return []

    placeholders = ",".join(["%s"] * len(ids))

    cursor.execute(f"""
        SELECT
            id,
            nombre,
            texto_pdf
        FROM documentos
        WHERE id IN ({placeholders})
    """, ids)

    return cursor.fetchall()


###########################################################
# LIMPIAR COLA
###########################################################

def limpiar_queue(cursor, ids):

    if not ids:
        return

    placeholders = ",".join(["%s"] * len(ids))

    cursor.execute(f"""
        DELETE FROM index_queue
        WHERE document_id IN ({placeholders})
    """, ids)


###########################################################
# LOOP PRINCIPAL
###########################################################

def loop():

    es = conectar_elastic()
    crear_indice(es)

    print("🚀 Daemon iniciado\n")

    while True:

        conexion = None

        try:

            # Se abre una conexión nueva en cada ciclo
            conexion = conectar_db()
            cursor = conexion.cursor()

            jobs = obtener_queue(cursor)

            if not jobs:

                print("Sin documentos pendientes...")

                time.sleep(INTERVALO)

                continue

            ids = [job["document_id"] for job in jobs]

            documentos = obtener_documentos(cursor, ids)

            print(f"Documentos a indexar: {len(documentos)}")

            indexar_documentos(es, documentos)

            #es.indices.refresh(index=INDEX)

            limpiar_queue(cursor, ids)

            conexion.commit()

            print(f"Procesados {len(documentos)} documentos.")

        except Exception as e:

            print("ERROR:", e)

            if conexion:
                conexion.rollback()

        finally:

            if conexion and conexion.open:
                conexion.close()

        time.sleep(INTERVALO)


###########################################################

if __name__ == "__main__":
    loop()