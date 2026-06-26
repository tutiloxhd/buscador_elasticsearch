from buscador import BuscadorElastic
from motor_reglas import MotorReglas


# Indexar datos


# Crear buscador
buscador = BuscadorElastic()

# Crear motor
motor = MotorReglas(buscador)

# Ejecutar reglas
resultados = motor.ejecutar()

print("\nTOTAL OBSERVACIONES:", len(resultados))