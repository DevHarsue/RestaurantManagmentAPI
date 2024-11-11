from sqlalchemy import create_engine,MetaData,Table
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
DATABASE = os.getenv("DATABASE")

engine = create_engine(f"postgresql+psycopg://{USER}:{PASSWORD}@{HOST}/{DATABASE}")
Session = sessionmaker(bind=engine)


metadata = MetaData()

mesas_ocupadas_table = Table('mesas_ocupadas', metadata, autoload_with=engine)
tipos_platos_table = Table('tipos_platos', metadata, autoload_with=engine)
platos_table = Table('platos', metadata, autoload_with=engine)
mesas_table = Table('mesas', metadata, autoload_with=engine)
ordenes_table = Table('ordenes', metadata, autoload_with=engine)
divisas_table = Table('divisas', metadata, autoload_with=engine)
detalles_ordenes_platos_table = Table('detalles_ordenes_platos', metadata, autoload_with=engine)
detalles_ordenes_divisas_table = Table('detalles_ordenes_divisas', metadata, autoload_with=engine)
clientes_table = Table('clientes', metadata, autoload_with=engine)
usuarios_table = Table('usuarios', metadata, autoload_with=engine)
roles_table = Table('roles', metadata, autoload_with=engine)
