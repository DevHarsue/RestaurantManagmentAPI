from fastapi import APIRouter,status
from fastapi.responses import JSONResponse
from typing import List
from ..models.divisa_model import Divisa
from ..database.actions.divisas_action import get_divisas_db

divisa_router = APIRouter()

@divisa_router.get("",status_code=status.HTTP_200_OK)
def get_divisas() -> List[Divisa]:
    divisas = get_divisas_db()
    contenido = [divisa.model_dump() for divisa in divisas]
    return JSONResponse(content=contenido,status_code=status.HTTP_200_OK)