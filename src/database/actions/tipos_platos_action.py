from typing import List
from ..connection import session
from ..schemas import TipoPlatoSchema
from ...models.tipo_plato_model import TipoPlato

def get_tipos_platos_db() -> List[TipoPlato]:
    result = session.query(TipoPlatoSchema).all()
    tipos_platos = [TipoPlato(
                        id=tipo_plato.tipo_plato_id,
                        nombre=tipo_plato.tipo_plato_nombre,
                        icon=tipo_plato.tipo_plato_icon)
                    for tipo_plato in result]
    
    return tipos_platos