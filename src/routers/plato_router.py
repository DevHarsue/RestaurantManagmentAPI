from fastapi import APIRouter,status
from fastapi.responses import JSONResponse
from typing import List
from ..models.plato_model import PlatoTipo
from ..database.actions.platos_action import get_platos_con_tipo_db

plato_router = APIRouter()

@plato_router.get("",status_code=status.HTTP_200_OK)
def get_platos_con_tipo() -> List[PlatoTipo]:
    platos = get_platos_con_tipo_db()
    contenido = [plato.model_dump() for plato in platos]
    return JSONResponse(content=contenido,status_code=status.HTTP_200_OK)