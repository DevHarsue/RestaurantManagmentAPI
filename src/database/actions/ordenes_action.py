from typing import List
from sqlalchemy import insert
from ..connection import Session,ordenes_table
from ...models.orden_model import Orden
from datetime import date

def get_ordenes_db() -> List[Orden]:
    with Session() as session:
        result = session.query(ordenes_table).all()
        ordenes = [Orden(
                    id=orden[0],
                    fecha=str(orden[1]),
                    cliente_id=orden[2]
                ) for orden in result]
        
        return ordenes
    
def insert_ordenes_db(cliente_id) -> Orden:
    with Session() as session:
        query = (insert(ordenes_table)
                        .values(cliente_id=cliente_id,orden_fecha=date.today())
                        .returning(*ordenes_table.columns)
                        )
        
        result = session.execute(query)
        orden = result.fetchone()
        session.commit()
        
        return Orden(id=orden.orden_id,fecha=str(orden.orden_fecha),cliente_id=orden.cliente_id)
