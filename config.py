import os

ELASTIC_URL = os.getenv("ELASTIC_URL", "http://localhost:9200")

INDEX_NAME = os.getenv("INDEX_NAME", "causas")