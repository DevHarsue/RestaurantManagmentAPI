from pydantic import BaseModel

class PlatoTipo(BaseModel):
    id: int
    nombre: str
    descripcion: str
    precio: float
    tipo_id: int
    icon: str
    
class PlatoTipoCantidad(BaseModel):
    plato_id: int
    nombre: str
    descripcion: str
    precio: float
    cantidad: int
    tipo_id: int
    icon: str