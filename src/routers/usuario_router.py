from fastapi import APIRouter,status,HTTPException
from fastapi.responses import JSONResponse
from ..models.usuario_model import UsuarioRegistro
from ..database.actions.usuarios_action import get_usuario_existe_db,insert_usuario_mesero_db
from .token_router import SECRET_KEY,ALGORITHM
from jose import jwt

usuario_router = APIRouter()

@usuario_router.post("/register_mesero",status_code=status.HTTP_200_OK)
def post_registrar_mesero(usuario: UsuarioRegistro) -> JSONResponse:
    buscar_usuario = get_usuario_existe_db(usuario.nombre)
    if buscar_usuario:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="Usuario Existente")
    
    usuario = insert_usuario_mesero_db(usuario)
    payload = usuario.model_dump()
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return JSONResponse(content={"access_token": token},status_code=status.HTTP_200_OK)
