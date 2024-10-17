from sqlalchemy import Column, Integer, String, Float,ForeignKey,DATE,CHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TipoPlatoSchema(Base):
    __tablename__ = 'tipos_platos'
    tipo_plato_id = Column(Integer, primary_key=True)
    tipo_plato_nombre = Column(String)
    tipo_plato_icon = Column(String)
    
class PlatoSchema(Base):
    __tablename__ = 'platos'
    plato_id = Column(Integer, primary_key=True)
    plato_nombre = Column(String)
    plato_descripcion = Column(String)
    plato_precio = Column(Float)
    tipo_plato_id = Column(Integer,ForeignKey('tipos_platos.tipo_plato_id'))

class MesaSchema(Base):
    __tablename__ = 'mesas'
    mesa_id = Column(Integer,primary_key=True)
    mesa_descripcion = Column(String)

class OrdenSchema(Base):
    __tablename__ = 'ordenes'
    orden_id = Column(Integer,primary_key=True)
    orden_fecha = Column(DATE)
    cliente_id = Column(Integer)
    
class MesaOcupadaSchema(Base):
    __tablename__ = 'mesas_ocupadas'
    mesa_id = Column(Integer,ForeignKey('mesas.mesa_id'),primary_key=True)
    orden_id = Column(Integer,ForeignKey('ordenes.orden_id'),primary_key=True)
    

class DivisaSchema(Base):
    __tablename__ = 'divisas'
    divisa_id = Column(Integer,primary_key=True)
    divisa_nombre = Column(String)
    divisa_relacion = Column(Float)
    
class DetalleOrdenPlatoSchema(Base):
    __tablename__ = 'detalles_ordenes_platos'
    detalle_orden_plato_id = Column(Integer,primary_key=True)
    orden_id = Column(Integer,ForeignKey('ordenes.orden_id'))
    plato_id = Column(Integer,ForeignKey('platos.plato_id'))
    detalle_orden_plato_cantidad = Column(Integer)
    
class DetalleOrdenDivisaSchema(Base):
    __tablename__ = 'detalles_ordenes_divisas'
    detalle_orden_divisa_id = Column(Integer,primary_key=True)
    orden_id = Column(Integer,ForeignKey('ordenes.orden_id'))
    divisa_id = Column(Integer,ForeignKey('divisas.divisa_id'))
    detalle_orden_divisa_cantidad = Column(Float)

class ClienteSchema(Base):
    __tablename__ = 'clientes'
    cliente_id = Column(Integer,primary_key=True)
    cliente_nacionalidad = Column(CHAR)
    cliente_cedula = Column(Integer)
    cliente_nombre = Column(String)
    cliente_apellido = Column(String)
    cliente_telefono = Column(String)
    cliente_direccion = Column(String)
    