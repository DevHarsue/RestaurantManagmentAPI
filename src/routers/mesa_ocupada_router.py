from fastapi import APIRouter,status
from fastapi.responses import JSONResponse
from typing import List
from sqlalchemy.exc import IntegrityError
from ..models.mesa_ocupada_model import MesaOcupada,MesaOcupadaCreate
from ..database.actions.mesas_ocupadas_action import get_mesas_ocupadas_db,insert_mesas_ocupadas_db

mesa_ocupada_router = APIRouter()

@mesa_ocupada_router.get("",status_code=status.HTTP_200_OK)
def get_mesas_ocupadas() -> List[MesaOcupada]:
    mesas_ocupadas = get_mesas_ocupadas_db()
    contenido = [mesa_ocupada.model_dump() for mesa_ocupada in mesas_ocupadas]
    return JSONResponse(content=contenido,status_code=status.HTTP_200_OK)

@mesa_ocupada_router.post("",status_code=status.HTTP_201_CREATED)
def insert_mesas_ocupadas(mesa_ocupada: MesaOcupadaCreate) -> MesaOcupada:
    try:
        mesa_ocupada = insert_mesas_ocupadas_db(mesa_ocupada.id,mesa_ocupada.orden_id)
    except IntegrityError:
        return JSONResponse(content={"Error":"ID's invalidos"}, status_code=status.HTTP_409_CONFLICT)
    
    return JSONResponse(content=mesa_ocupada.model_dump(),status_code=status.HTTP_201_CREATED)