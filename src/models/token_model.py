from pydantic import BaseModel,validator

class Usuario(BaseModel):
    nombre: str
    contraseña: str
    rol: str | None = None