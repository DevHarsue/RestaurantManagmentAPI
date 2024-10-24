from fastapi import APIRouter,status
from fastapi.responses import JSONResponse
from typing import List
from sqlalchemy.exc import IntegrityError
from ..models.orden_model import Orden,OrdenCreate
from ..database.actions.ordenes_action import get_ordenes_db,insert_ordenes_db

orden_router = APIRouter()

@orden_router.get("",status_code=status.HTTP_200_OK)
def get_ordenes() -> List[Orden]:
    ordenes = get_ordenes_db()
    contenido = [orden.model_dump() for orden in ordenes]
    return JSONResponse(content=contenido,status_code=status.HTTP_200_OK)

@orden_router.post("",status_code=status.HTTP_201_CREATED)
def insert_ordenes(orden: OrdenCreate) -> Orden:
    try:
        orden = insert_ordenes_db(orden.cliente_id)
    except IntegrityError:
        return JSONResponse(content={"Error":"ID del cliente invalido"}, status_code=status.HTTP_409_CONFLICT)
    
    return JSONResponse(content=orden.model_dump(),status_code=status.HTTP_201_CREATED)