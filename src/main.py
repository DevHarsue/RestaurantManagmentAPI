from fastapi import FastAPI,status
from fastapi.responses import JSONResponse
from src.routers.plato_router import plato_router
from src.routers.tipo_plato_router import tipo_plato_router

app = FastAPI()

@app.get("/",tags=["Home"],status_code=status.HTTP_200_OK)
def home() -> JSONResponse:
    return JSONResponse(content={"Mensaje": "API para Restaurante"},status_code=status.HTTP_200_OK)

app.include_router(router=plato_router,prefix="/platos",tags=["Platos"])
app.include_router(router=tipo_plato_router,prefix="/tipos_platos",tags=["TiposPlatos"])