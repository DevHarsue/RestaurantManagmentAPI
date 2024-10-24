from pydantic import BaseModel,validator
from datetime import date

class Orden(BaseModel):
    id: int
    fecha: str
    cliente_id: int | None=None

class OrdenCreate(BaseModel):
    cliente_id: int | None=None
    
    @validator("cliente_id")
    def validate_cliente_id(cls,value):
        if value==None:
            return None
        
        if value <= 0:
            raise ValueError("El id del cliente debe ser mayor a 0")
        
        return value
    
    model_config = {
        "json_schema_extra": {
            'example': {
                "cliente_id": 1
            }
        }
    }