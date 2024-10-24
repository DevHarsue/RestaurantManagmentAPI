from typing import List
from sqlalchemy import insert
from ..connection import Session,mesas_ocupadas_table
from ...models.mesa_ocupada_model import MesaOcupada

def get_mesas_ocupadas_db() -> List[MesaOcupada]:
    with Session() as session:
        result = session.query(mesas_ocupadas_table).all()
        mesas_ocupadas = [MesaOcupada(
                    id=mesa_ocupada[0],
                    orden_id=mesa_ocupada[1]
                ) for mesa_ocupada in result]
        
        return mesas_ocupadas

def insert_mesas_ocupadas_db(mesa_id,orden_id) -> MesaOcupada:
    with Session() as session:
        query = (insert(mesas_ocupadas_table)
                    .values(mesa_id=mesa_id,orden_id=orden_id)
                    .returning(*mesas_ocupadas_table.columns)
                    )
        
        result = session.execute(query)
        mesa_ocupada = result.fetchone()
        session.commit()
        return MesaOcupada(id=mesa_ocupada.mesa_id,orden_id=mesa_ocupada.orden_id)
