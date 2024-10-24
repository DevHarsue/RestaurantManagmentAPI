from pydantic import BaseModel,validator

class MesaOcupada(BaseModel):
    id: int
    orden_id: int

class MesaOcupadaCreate(MesaOcupada):
    @validator("id")
    def validate_id(cls,value):
        if value <= 0:
            raise ValueError("El id de la mesa debe ser mayor que 0")
        return value
    @validator("orden_id")
    def validate_orden_id(cls,value):
        if value <= 0:
            raise ValueError("El orden_id de la mesa debe ser mayor que 0")
        return value
    model_config = {
        "json_schema_extra": {
            'example': {
                "id": 1,
                "orden_id": 1
            }
        }
    }