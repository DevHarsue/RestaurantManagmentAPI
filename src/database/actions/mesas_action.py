from typing import List
from ..connection import Session,mesas_table
from ...models.mesa_model import Mesa

def get_mesas_db() -> List[Mesa]:
    with Session() as session:
        result = session.query(mesas_table).all()
        mesas = [Mesa(
                    id=mesa[0],
                    descripcion=mesa[1])
                    for mesa in result]
        
        return mesas