from typing import List
from sqlalchemy import join,select
from ..connection import Session,platos_table,tipos_platos_table
from ...models.plato_model import PlatoTipo

def get_platos_con_tipo_db() -> List[PlatoTipo]:
    with Session() as session:
        j = join(   
                    platos_table,tipos_platos_table,
                    platos_table.c.tipo_plato_id==tipos_platos_table.c.tipo_plato_id
                )
        query = select(platos_table,tipos_platos_table.c.tipo_plato_icon).select_from(j)

        result = session.execute(query).fetchall()
        platos = [PlatoTipo(
                    id=plato[0],
                    nombre=plato[1],
                    descripcion=plato[2],
                    precio=plato[3],
                    tipo_id=plato[4],
                    icon=plato[5])
                    for plato in result]

        return platos
