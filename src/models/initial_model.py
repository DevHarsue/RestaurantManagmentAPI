from pydantic import BaseModel
from typing import List,Dict
from .divisa_model import Divisa
from .mesa_model import Mesa
from .mesa_ocupada_model import MesaOcupada
from .plato_model import PlatoTipo
from .tipo_plato_model import TipoPlato

class InitialPlatos(BaseModel):
    platos_tipos : List[PlatoTipo]
    tipos_platos: List[TipoPlato]

class InitialMesas(BaseModel):
    mesas: List[Mesa]
    mesas_ocupadas: List[MesaOcupada]

class InitialDataAndroid(BaseModel):
    section_divisas: List[Divisa]
    section_mesas: InitialMesas
    section_platos: InitialPlatos

