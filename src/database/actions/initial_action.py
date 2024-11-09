from ...models.initial_model import InitialDataAndroid,InitialMesas,InitialPlatos
from .divisas_action import get_divisas_db
from .mesas_action import get_mesas_db
from .mesas_ocupadas_action import get_mesas_ocupadas_db
from .platos_action import get_platos_con_tipo_db
from .tipos_platos_action import get_tipos_platos_db

def get_initial_data_android_db() -> InitialDataAndroid:
    divisas = get_divisas_db()
    mesas = get_mesas_db()
    mesas_ocupadas = get_mesas_ocupadas_db()
    platos = get_platos_con_tipo_db()
    tipos_platos = get_tipos_platos_db()
    data = InitialDataAndroid(
                section_divisas=divisas,
                section_mesas=InitialMesas(mesas=mesas,mesas_ocupadas=mesas_ocupadas),
                section_platos=InitialPlatos(platos_tipos=platos,tipos_platos=tipos_platos)
                )
    return data
    