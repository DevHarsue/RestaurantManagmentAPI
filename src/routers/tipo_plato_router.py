from fastapi import APIRouter,status
from fastapi.responses import JSONResponse
from typing import List
from ..models.tipo_plato_model import TipoPlato
from ..database.actions.tipos_platos_action import get_tipos_platos_db

tipo_plato_router = APIRouter()

@tipo_plato_router.get("",status_code=status.HTTP_200_OK)
def get_tipos_platos() -> List[TipoPlato]:
    tipos_platos = get_tipos_platos_db()
    contenido = [tipo_plato.model_dump() for tipo_plato in tipos_platos]
    return JSONResponse(content=contenido,status_code=status.HTTP_200_OK)