from fastapi import APIRouter,status
from fastapi.responses import JSONResponse
from typing import List
from ..models.mesa_model import Mesa
from ..database.actions.mesas_action import get_mesas_db

mesa_router = APIRouter()

@mesa_router.get("",status_code=status.HTTP_200_OK)
def get_mesas() -> List[Mesa]:
    mesas = get_mesas_db()
    contenido = [mesa.model_dump() for mesa in mesas]
    return JSONResponse(content=contenido,status_code=status.HTTP_200_OK)