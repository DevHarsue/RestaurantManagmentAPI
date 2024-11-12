from pydantic import BaseModel,validator
import re

class Usuario(BaseModel):
    nombre: str
    contraseña: str
    rol: str | None = None

class UsuarioRegistro(BaseModel):
    nombre: str
    contraseña: str
    
    @validator("nombre")
    def validate_nombre(cls,value: str):
        regex = r"^(?=.*[a-zA-Z])[a-zA-Z0-9]{5,16}$"
        if not re.match(regex, value):
            raise ValueError("El nombre de usuario debe contener almenos una letra, no puede tener caracteres especiales y tiene que tener una longitud entre 5 y 16 caracteres")
        return value.upper()
    
    @validator("contraseña")
    def validate_contraseña(cls,value):
        regex = r"^(?=(?:.*[a-zA-Z]){2})(?=(?:.*\d){2})(?=.*[!@#$%^&_.,:;+=*])[a-zA-Z\d!@#$%^&_.,:;+=*]{8,16}$"
        if not re.match(regex, value):
            raise ValueError("La contraseña debe contener almenos dos letras, dos numeros, un caracter especial (validos: !@#$%^&_.,:;+=*) y tiene que tener una longitud entre 8 y 16 caracteres")
        return value