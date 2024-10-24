from pydantic import BaseModel,validator
from typing import List


class DetalleOrdenPlato(BaseModel):
    plato_id: int
    cantidad: int

    @validator('plato_id')
    def validate_plato_id(cls, v):
        if v <= 0:
            raise ValueError('El id del plato debe ser mayor a 0')
        return v
    
    @validator('cantidad')
    def validate_cantidad(cls, v):
        if v <= 0:
            raise ValueError('La cantidad debe ser mayor a 0')
        return v
    
class DetallesOrdenPlatos(BaseModel):
    orden_id: int
    platos: List[DetalleOrdenPlato]
    @validator('orden_id')
    def validate_orden_id(cls, v):
        if v <= 0:
            raise ValueError('El id de la orden debe ser mayor a 0')
        return v

class DetalleOrdenPlatoUpdate(BaseModel):
    orden_id: int
    plato_id: int
    cantidad: int
    
    @validator('orden_id')
    def validate_orden_id(cls, v):
        if v <= 0:
            raise ValueError('El id de la orden debe ser mayor a 0')
        return v
    
    @validator('plato_id')
    def validate_plato_id(cls, v):
        if v <= 0:
            raise ValueError('El id del plato debe ser mayor a 0')
        return v
