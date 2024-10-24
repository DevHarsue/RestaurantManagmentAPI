from pydantic import BaseModel

class Mesa(BaseModel):
    id: int
    descripcion: str