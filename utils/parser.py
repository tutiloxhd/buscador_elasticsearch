def parse_documentos(data):

    documentos = []

    detalle = data["resultado"]["detalle_causa"]

    encabezado = detalle["encabezado"]

    cuadernos = detalle["cuadernos"]

    for nombre_cuaderno, movimientos in cuadernos.items():

        for movimiento in movimientos:

            docs = movimiento.get("Documentos", {})

            texto = docs.get("texto_extraído")

            if not texto:
                continue

            documentos.append({

                "id_propiedad": encabezado["ID_PROPIEDAD"],

                "rol": encabezado["ROL"],

                "tribunal": encabezado["Tribunal"],

                "cuaderno": nombre_cuaderno,

                "folio": movimiento.get("Folio"),

                "fecha": movimiento.get("Fec_Tramite"),

                "tramite": movimiento.get("Tramite"),

                "descripcion": movimiento.get("Desc_Tramite"),

                "pdf": docs.get("pdf"),

                "texto": texto

            })

    return documentos