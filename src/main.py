from fastapi import FastAPI,status,Request,Response,Body,Depends,APIRouter,HTTPException
from fastapi.responses import JSONResponse
from src.routers.plato_router import plato_router
from src.routers.tipo_plato_router import tipo_plato_router
from src.routers.mesa_router import mesa_router
from src.routers.divisa_router import divisa_router
from src.routers.mesa_ocupada_router import mesa_ocupada_router
from src.routers.initial_router import initial_router
from src.routers.orden_router import orden_router
from src.routers.detalle_orden_plato_router import detalle_orden_plato_router
from src.routers.usuario_router import usuario_router
from src.routers.token_router import token_router,decode_token,depend_rol
from src.database.connection import HOST,USER,PASSWORD,DATABASE
import psycopg
from psycopg.rows import dict_row

app = FastAPI()

@app.middleware("http")
async def http_error_handler(request: Request,call_next) -> Response | JSONResponse:
    try:
        return await call_next(request)
    except Exception as e:
        content = {"Error_text": str(e),"Class": str(e.__class__)}
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return JSONResponse(content=content, status_code=status_code)

@app.get("/",tags=["Home"],status_code=status.HTTP_200_OK)
def home() -> JSONResponse:
    return JSONResponse(content={"Mensaje": "API para Restaurante"},status_code=status.HTTP_200_OK)

app.include_router(router=token_router,prefix="/token",tags=["TOKEN"])

routers = APIRouter(dependencies=[Depends(decode_token)])

@routers.post("/execute")
def execute(rol:depend_rol,sql:str = Body()):
    if rol!="SUPERADMIN":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="No Autorizado")
    with psycopg.connect(
                            user=USER,
                            password=PASSWORD,
                            host=HOST,
                            dbname=DATABASE) as conn:
        cursor = conn.cursor(row_factory=dict_row)
        cursor.execute(sql)
        datos = cursor.fetchall()
    return JSONResponse(content=datos,status_code=status.HTTP_200_OK)

routers.include_router(router=plato_router,prefix="/platos",tags=["Platos"])
routers.include_router(router=tipo_plato_router,prefix="/tipos_platos",tags=["TiposPlatos"])
routers.include_router(router=mesa_router,prefix="/mesas",tags=["Mesas"])
routers.include_router(router=divisa_router,prefix="/divisas",tags=["Divisas"])
routers.include_router(router=mesa_ocupada_router,prefix="/mesas_ocupadas",tags=["MesasOcupadas"])
routers.include_router(router=orden_router,prefix="/ordenes",tags=["Ordenes"])
routers.include_router(router=detalle_orden_plato_router,prefix="/detalles_ordenes_platos",tags=["DetallesOrdenesPlatos"])
routers.include_router(router=initial_router,prefix="/initial",tags=["Initial"])
routers.include_router(router=usuario_router,prefix="/usuarios",tags=["Usuarios"])

app.include_router(routers)