from fastapi import APIRouter,status
from fastapi.responses import JSONResponse
from ..models.initial_model import InitialDataAndroid
from ..database.actions.initial_action import get_initial_data_android_db

initial_router = APIRouter()

@initial_router.get("/android",status_code=status.HTTP_200_OK)
def get_initial_data_android() -> InitialDataAndroid:
    data = get_initial_data_android_db()
    contenido = data.model_dump()
    return JSONResponse(content=contenido,status_code=status.HTTP_200_OK)
    