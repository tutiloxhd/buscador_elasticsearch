from fastapi import FastAPI

from routes.index import router as index_router
from routes.search import router as search_router

from elastic.mappings import create_index

app = FastAPI(
    title="Elasticsearch Service",
    version="1.0.0"
)


@app.on_event("startup")
def startup():

    create_index()


app.include_router(index_router)

app.include_router(search_router)