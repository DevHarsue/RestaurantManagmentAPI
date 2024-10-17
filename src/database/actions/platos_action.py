from typing import List
from sqlalchemy import join,select
from ..connection import session
from ..schemas import TipoPlatoSchema,PlatoSchema
from ...models.plato_model import Plato

def get_platos_con_tipo_db() -> List[Plato]:
    j = join(PlatoSchema,TipoPlatoSchema,PlatoSchema.tipo_plato_id==TipoPlatoSchema.tipo_plato_id)
    query = select(PlatoSchema,TipoPlatoSchema).select_from(j)

    result = session.execute(query)
    
    platos = [Plato(
                id=plato.plato_id,
                nombre=plato.plato_nombre,
                descripcion=plato.plato_descripcion,
                precio=plato.plato_precio,
                tipo_id=tipo.tipo_plato_id,
                icon=tipo.tipo_plato_icon)
            for plato,tipo in result]

    return platos
