from typing import List
from sqlalchemy import insert,text,update
from ..connection import Session,detalles_ordenes_platos_table
from ...models.plato_model import PlatoTipoCantidad
from ...models.detalle_orden_plato_model import DetallesOrdenPlatos,DetalleOrdenPlatoUpdate

def get_detalles_ordenes_platos_by_orden_db(orden_id) -> List[PlatoTipoCantidad]:
    with Session() as session:
        text_sql = f"""
                        SELECT 
                            dop.plato_id,
                            p.plato_nombre,
                            p.plato_descripcion,
                            p.plato_precio,
                            dop.detalle_orden_plato_cantidad,
                            tp.tipo_plato_id,
                            tp.tipo_plato_icon
                        FROM detalles_ordenes_platos as dop
                        JOIN platos as p 
                            ON p.plato_id=dop.plato_id 
                        JOIN tipos_platos as tp
                            ON tp.tipo_plato_id = p.tipo_plato_id 
                        WHERE dop.orden_id = :orden_id;"""
        result = session.execute(text(text_sql),{"orden_id":orden_id}).fetchall()
        detalles_platos = [PlatoTipoCantidad(
                            plato_id=detalle_plato[0],
                            nombre=detalle_plato[1],
                            descripcion=detalle_plato[2],
                            precio=detalle_plato[3],
                            cantidad=detalle_plato[4],
                            tipo_id=detalle_plato[5],
                            icon=detalle_plato[6],
                        ) for detalle_plato in result]
        
        return detalles_platos

    
def insert_detalles_ordenes_platos_db(detalles: DetallesOrdenPlatos) -> DetallesOrdenPlatos:
    data = [{"orden_id":detalles.orden_id,"plato_id":d.plato_id,"detalle_orden_plato_cantidad":d.cantidad} for d in detalles.platos]
    with Session() as session:
        query = detalles_ordenes_platos_table.insert().returning(
            detalles_ordenes_platos_table.c.orden_id,
            detalles_ordenes_platos_table.c.plato_id,
            detalles_ordenes_platos_table.c.detalle_orden_plato_cantidad).values(data)
        
        result = session.execute(query).fetchall()
        detalles = DetallesOrdenPlatos(orden_id=result[0][0],
                                            platos=[{"plato_id":p[1],"cantidad":p[2]} for p in result])
        session.commit()
        
        return detalles

def update_detalles_ordenes_platos_cantidad_db(detalle: DetalleOrdenPlatoUpdate) -> DetalleOrdenPlatoUpdate:
    with Session() as session:
        query = update(detalles_ordenes_platos_table).where(
                detalles_ordenes_platos_table.c.orden_id == detalle.orden_id,
            ).where(
                detalles_ordenes_platos_table.c.plato_id == detalle.plato_id,
            ).values(detalle_orden_plato_cantidad=detalles_ordenes_platos_table.c.detalle_orden_plato_cantidad+detalle.cantidad
            ).returning(
                detalles_ordenes_platos_table.c.orden_id,
                detalles_ordenes_platos_table.c.plato_id,
                detalles_ordenes_platos_table.c.detalle_orden_plato_cantidad
            )
        result = session.execute(query).fetchone()
        if not bool(result):
            return None
        detalle = DetalleOrdenPlatoUpdate(orden_id=result[0],plato_id=result[1],cantidad=result[2])
        session.commit()
        
        return detalle