from elasticsearch import Elasticsearch
from config import ELASTIC_URL

es = Elasticsearch(ELASTIC_URL)

def get_client():
    return es