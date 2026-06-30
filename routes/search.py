from fastapi import APIRouter, HTTPException

from services.search_service import buscar

router = APIRouter()


@router.post("/buscar")
def buscar_documentos(body: dict):

    try:

        terminos = body["terminos"]

        size = body.get("size", 20)

        return buscar(terminos, size)

    except Exception as e:

        raise HTTPException(status_code=500, detail=str(e))