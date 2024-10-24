from typing import List
from ..connection import Session,tipos_platos_table
from ...models.tipo_plato_model import TipoPlato

def get_tipos_platos_db() -> List[TipoPlato]:
    with Session() as session:
        result = session.query(tipos_platos_table).all()
        tipos_platos = [TipoPlato(
                            id=tipo_plato[0],
                            nombre=tipo_plato[1],
                            icon=tipo_plato[2])
                        for tipo_plato in result]
        
        return tipos_platos