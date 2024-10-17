from pydantic import BaseModel

class TipoPlato(BaseModel):
    id: int
    nombre: str
    icon: str