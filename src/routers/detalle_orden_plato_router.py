from fastapi import APIRouter,status,Query
from fastapi.responses import JSONResponse
from typing import List
from sqlalchemy.exc import IntegrityError
from ..models.plato_model import PlatoTipoCantidad
from ..models.detalle_orden_plato_model import DetallesOrdenPlatos,DetalleOrdenPlatoUpdate
from ..database.actions.detalles_ordenes_platos_actions import (
    get_detalles_ordenes_platos_by_orden_db,
    insert_detalles_ordenes_platos_db,
    update_detalles_ordenes_platos_cantidad_db)

detalle_orden_plato_router = APIRouter()

@detalle_orden_plato_router.get("",status_code=status.HTTP_200_OK)
def get_detalles_ordenes_platos_by_orden(orden_id:int = Query(gt=0)) -> List[PlatoTipoCantidad]:
    detalles_orden_platos = get_detalles_ordenes_platos_by_orden_db(orden_id)
    contenido = [detalle_orden.model_dump() for detalle_orden in detalles_orden_platos]
    return JSONResponse(content=contenido,status_code=status.HTTP_200_OK)

@detalle_orden_plato_router.post("",status_code=status.HTTP_201_CREATED)
def insert_detalles_ordenes_platos(detalles: DetallesOrdenPlatos) -> DetallesOrdenPlatos:
    try:
        detalles_orden_plato = insert_detalles_ordenes_platos_db(detalles)
    except IntegrityError:
        return JSONResponse(content={"Error":"ID's invalidos"}, status_code=status.HTTP_409_CONFLICT)
    
    return JSONResponse(content=detalles_orden_plato.model_dump(),status_code=status.HTTP_201_CREATED)

@detalle_orden_plato_router.put("",status_code=status.HTTP_200_OK)
def update_detalles_ordenes_platos_cantidad_(detalles: DetalleOrdenPlatoUpdate) -> DetalleOrdenPlatoUpdate:
    try:
        detalles_orden_plato = update_detalles_ordenes_platos_cantidad_db(detalles)
        if not detalles_orden_plato:
            return JSONResponse(content={"Error":"No se encontraron detalles de orden"}, status_code=status.HTTP_404_NOT_FOUND)
    except IntegrityError:
        return JSONResponse(content={"Error":"ID's invalidos"}, status_code=status.HTTP_409_CONFLICT)
    
    return JSONResponse(content=detalles_orden_plato.model_dump(),status_code=status.HTTP_200_OK)