from ..connection import Session,usuarios_table,roles_table
from sqlalchemy import join,select
from ...models.token_model import Usuario
import hashlib
import os

def hashear(password:str,salt:str=None) -> dict:
    salt = os.urandom(16) if not salt else bytes.fromhex(salt)
    hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'),salt,100000)
    hash_hex = hash.hex()
    salt_hex = salt.hex()
    return {"password":hash_hex,"salt":salt_hex}

def get_usuario_db(usuario: Usuario) -> Usuario | None:
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
        if usuario_db.usuario_contraseña == hashear(usuario.contraseña,usuario_db.usuario_salt)["password"]:
            usuario.rol = usuario_db.rol_nombre
            return usuario
        
        