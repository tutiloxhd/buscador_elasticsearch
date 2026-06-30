## Descripción

Prueba de concepto para indexación y búsqueda de documentos utilizando:

- Python 3
- MariaDB
- Elasticsearch

El objetivo es demostrar una arquitectura donde:

Documento → MariaDB → Trigger → Cola de indexación → Elasticsearch → Motor de reglas

La indexación es incremental: solamente los documentos nuevos son enviados a Elasticsearch.


# Instalación

## Windows

### 1. Clonar repositorio

```bash
git clone <repositorio>

cd proyecto
```

### 2. Crear entorno virtual

```bash
python -m venv .venv
```

Activar

```bash
.venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Linux

### 1. Clonar

```bash
git clone <repositorio>

cd proyecto
```

### 2. Crear entorno

```bash
python3 -m venv .venv
```

Activar

```bash
source .venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---
Crear una base de datos.

Ejecutar:

```
sql/schema.sql
```

Posteriormente ejecutar:

```
sql/trigger.sql
```

---

# Instalación de Elasticsearch

## Windows

Descargar Elasticsearch desde Elastic.

Descomprimir.

Iniciar:

```cmd
bin\elasticsearch.bat
```

---

## Linux

Descargar Elasticsearch.

Descomprimir.

Ejecutar:

```bash
./bin/elasticsearch
```

---

Verificar funcionamiento

Abrir:

```
http://localhost:9200
```

Debe responder información del nodo.

---

# Configuración

Editar

```
config.py
```

Completar:

```python
DB_CONFIG = {

    "host": "...",
    "user": "...",
    "password": "...",
    "database": "..."
}

ELASTIC_URL = "http://localhost:9200"

INDEX = "documentos"
```

---

# Levantar el indexador

En una terminal:

```bash
python daemon_indexador.py
```

El proceso queda ejecutándose permanentemente.

Cada nuevo INSERT será indexado automáticamente.

---

# Ejecutar motor de reglas

En otra terminal:

```bash
python main.py
```

El motor consultará Elasticsearch utilizando las reglas configuradas.

---
# Agregar nuevas reglas

Editar:

```
motor_reglas.py
```

Agregar una nueva regla:

```python
{
    "nombre": "HIPOTECA",
    "termino": "hipoteca",
    "motivo": "El documento contiene la palabra hipoteca."
}
```

No es necesario volver a indexar documentos.

---
