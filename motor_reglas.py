from buscador import BuscadorElastic


class MotorReglas:

    def __init__(self, buscador: BuscadorElastic):

        self.buscador = buscador

        # Reglas iniciales (luego esto puede venir de BD)
        self.reglas = [
            {
                "nombre": "USUFRUCTO",
                "termino": "usufructo",
                "motivo": "El documento contiene la palabra usufructo."
            },
            {
                "nombre": "SERVIDUMBRE",
                "termino": "servidumbre",
                "motivo": "El documento contiene la palabra servidumbre."
            },
            {
                "nombre": "HIPOTECA",
                "termino": "hipoteca",
                "motivo": "El documento contiene la palabra hipoteca."
            }
        ]

        print("Motor de reglas inicializado.")

    ###########################################################
    # EJECUCIÓN PRINCIPAL
    ###########################################################

    def ejecutar(self):

        print("\nEjecutando reglas...\n")

        observaciones = []

        for regla in self.reglas:

            resultados = self.buscador.buscar(regla["termino"])

            if resultados:

                for r in resultados:

                    observacion = {
                        "regla": regla["nombre"],
                        "motivo": regla["motivo"],
                        "documento_id": r["id"],
                        "documento_nombre": r["nombre"],
                        "fragmento": r["fragmento"]
                    }

                    observaciones.append(observacion)

                    self._imprimir_observacion(observacion)

        print("\nProceso de reglas finalizado.")

        return observaciones

    ###########################################################
    # OUTPUT FORMATEADO
    ###########################################################

    def _imprimir_observacion(self, obs):

        print("=" * 60)
        print(f"REGLA     : {obs['regla']}")
        print(f"DOCUMENTO : {obs['documento_nombre']}")
        print(f"ID        : {obs['documento_id']}")
        print(f"MOTIVO    : {obs['motivo']}")
        print(f"FRAGMENTO : {obs['fragmento']}")
        print("=" * 60)