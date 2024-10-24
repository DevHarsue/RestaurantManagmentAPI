from pydantic import BaseModel

class Divisa(BaseModel):
    id: int
    nombre: str
    relacion: float