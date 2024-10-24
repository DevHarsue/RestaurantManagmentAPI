from typing import List
from ..connection import Session,divisas_table
from ...models.divisa_model import Divisa

def get_divisas_db() -> List[Divisa]:
    with Session() as session:
        result = session.query(divisas_table).where(divisas_table.c.divisa_id>=2)
        divisas = [Divisa(
                    id=divisa[0],
                    nombre=divisa[1],
                    relacion=divisa[2]
                ) for divisa in result]
        
        return divisas
