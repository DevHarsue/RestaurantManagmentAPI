from pydantic import BaseModel

class Plato(BaseModel):
    id: int
    nombre: str
    descripcion: str
    precio: float
    tipo_id: int
    icon: str