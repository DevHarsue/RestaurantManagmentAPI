from fastapi import FastAPI,status,Request,Response
from fastapi.responses import JSONResponse
from src.routers.plato_router import plato_router
from src.routers.tipo_plato_router import tipo_plato_router
from src.routers.mesa_router import mesa_router
from src.routers.divisa_router import divisa_router
from src.routers.mesa_ocupada_router import mesa_ocupada_router
from src.routers.orden_router import orden_router
from src.routers.detalle_orden_plato_router import detalle_orden_plato_router

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

app.include_router(router=plato_router,prefix="/platos",tags=["Platos"])
app.include_router(router=tipo_plato_router,prefix="/tipos_platos",tags=["TiposPlatos"])
app.include_router(router=mesa_router,prefix="/mesas",tags=["Mesas"])
app.include_router(router=divisa_router,prefix="/divisas",tags=["Divisas"])
app.include_router(router=mesa_ocupada_router,prefix="/mesas_ocupadas",tags=["MesasOcupadas"])
app.include_router(router=orden_router,prefix="/ordenes",tags=["Ordenes"])
app.include_router(router=detalle_orden_plato_router,prefix="/detalles_ordenes_platos",tags=["DetallesOrdenesPlatos"])