from pathlib import Path
import mariadb

# ==========================
# Configuración
# ==========================
CARPETA_TXT = Path(r"ruta/a/tu/carpeta/de/archivos/txt")

conn = mariadb.connect(
    host="localhost",
    user="root",
    password="Admi2465",
    database="pruebas_busqueda"
)

cursor = conn.cursor()

# Si la tabla está vacía y quieres que el primer id sea 5
cursor.execute("ALTER TABLE documentos AUTO_INCREMENT = 5")

# ==========================
# Inserción masiva
# ==========================
sql = """
INSERT INTO documentos (nombre, texto_pdf)
VALUES (?, ?)
"""

cantidad = 0

for archivo in CARPETA_TXT.glob("*.txt"):
    with open(archivo, "r", encoding="utf-8", errors="ignore") as f:
        contenido = f.read()

    cursor.execute(
        sql,
        (archivo.stem, contenido)
    )

    cantidad += 1
    print(f"Insertado: {archivo.name}")

conn.commit()

print(f"\nSe insertaron {cantidad} documentos.")

cursor.close()
conn.close()