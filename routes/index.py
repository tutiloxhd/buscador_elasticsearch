from fastapi import APIRouter, HTTPException

from services.index_service import indexar

router = APIRouter()


@router.post("/indexar")
def indexar_documentos(data: dict):

    try:
        resultado = indexar(data)
        return resultado

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))