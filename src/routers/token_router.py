from fastapi import APIRouter,HTTPException,status,Depends,Form,Request,Query
from fastapi.responses import JSONResponse
from typing import Annotated,List
from fastapi.security import OAuth2PasswordBearer
from src.models.token_model import Usuario
from ..database.actions.token_action import get_usuario_db
from jose import jwt
import os

token_router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

def get_rol(request: Request):
    return request.state.data

depend_rol = Annotated[str,Depends(get_rol)]

class CustomOAuth2PasswordRequestForm:
    def __init__(self, username: str = Form(...), password: str = Form(...)):
        self.username = username.upper()
        self.password = password

def decode_token(request: Request,token: str = Depends(oauth2_scheme)) -> None:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        usuario = get_usuario_db(Usuario(nombre=payload["nombre"],contraseña=payload["contraseña"]))
        
        if not usuario:
            raise Exception()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token Invalido"
            )
    
    request.state.data = usuario.rol

        
@token_router.post("",status_code=status.HTTP_200_OK)
async def login(form_data: Annotated[CustomOAuth2PasswordRequestForm,Depends()]) -> JSONResponse:
    usuario = get_usuario_db(Usuario(nombre=form_data.username,contraseña=form_data.password))
    if not bool(usuario):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario o Contraseña Incorrecta")
        
    payload = usuario.model_dump()
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return JSONResponse(content={"access_token": token},status_code=status.HTTP_200_OK)


# @token_router.post("/token/register",status_code=status.HTTP_200_OK)
# async def register(_: Annotated[None,Depends(decode_token)],rol: depend_rol,form_data: Usuario= Form(...)) -> JSONResponse:
#     if rol!="SUPERADMIN":
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="No Autorizado")
        
#     for user in users:
#         if user.username == form_data.username:
#             raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="Usuario Existente")
    
#     users.append(form_data)
#     payload = form_data.model_dump()
#     token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
#     return JSONResponse(content={"access_token": token},status_code=status.HTTP_200_OK)

# @token_router.get("/token/users",status_code=status.HTTP_200_OK)
# def get_users(_: Annotated[None,Depends(decode_token)],rol: depend_rol)-> List[Usuario]:
#     if rol!="SUPERADMIN":
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="No Autorizado")
    
#     return JSONResponse(content=[user.model_dump() for user in users],status_code=status.HTTP_200_OK)

# @token_router.delete("/token/users",status_code=status.HTTP_200_OK)
# def delete_user(_: Annotated[None,Depends(decode_token)],rol: depend_rol,username: str = Query())-> Usuario:
#     if rol!="SUPERADMIN":
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="No Autorizado")
    
#     usuario = None
#     for user in users:
#         if user.username == username:
#             usuario = user
#             users.remove(user)
#             break
#     if not usuario:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Usuario No Encontrado")
    
#     return JSONResponse(content=usuario.model_dump(),status_code=status.HTTP_200_OK)
