from ..connection import Session,usuarios_table,roles_table
from sqlalchemy import join,select,insert
from ...models.usuario_model import Usuario,UsuarioRegistro
import hashlib
import os

def hashear(password:str,salt:str=None) -> dict:
    salt = os.urandom(16) if not salt else bytes.fromhex(salt)
    hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'),salt,100000)
    hash_hex = hash.hex()
    salt_hex = salt.hex()
    return {"password":hash_hex,"salt":salt_hex}

def get_usuario_db(usuario: Usuario,is_hash=False) -> Usuario | None:
    with Session() as session:
        j = join(
                    usuarios_table,roles_table,
                    usuarios_table.c.rol_id == roles_table.c.rol_id
                )
        query = select(
                        usuarios_table.c.usuario_nombre,
                        usuarios_table.c.usuario_contraseña,
                        usuarios_table.c.usuario_salt,
                        roles_table.c.rol_nombre
                        ).select_from(j).where(usuario.nombre==usuarios_table.c.usuario_nombre)
        usuario_db = session.execute(query).fetchone()
        if not usuario_db:
            return None
        password = hashear(usuario.contraseña,usuario_db.usuario_salt)["password"] if not is_hash else usuario.contraseña 
        if usuario_db.usuario_contraseña == password:
            usuario.rol = usuario_db.rol_nombre
            usuario.contraseña = usuario_db.usuario_contraseña
            return usuario
        return None

def get_usuario_existe_db(usuario_nombre:str) -> str | None:
    with Session() as session:
        query = select(usuarios_table.c.usuario_nombre).where(usuario_nombre==usuarios_table.c.usuario_nombre)
        data = session.execute(query).fetchone()
        if not data:
            return None
        return data.usuario_nombre

def insert_usuario_mesero_db(usuario: UsuarioRegistro) -> Usuario:
    with Session() as session:
        hash = hashear(usuario.contraseña)
        query = insert(usuarios_table).values(
            usuario_nombre=usuario.nombre,
            usuario_contraseña=hash["password"],
            usuario_salt=hash["salt"],
            rol_id=4
        ).returning(usuarios_table.c.usuario_nombre)
        nombre = session.execute(query).fetchone()
        session.commit()
    usuario = get_usuario_db(Usuario(nombre=nombre[0],contraseña=usuario.contraseña))
    return usuario