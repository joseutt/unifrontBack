from sqlalchemy.orm import Session
from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioCreate
from app.core.security import (
    hash_password
)

def get_usuarios(db: Session):
    return db.query(Usuario).all()

def get_usuario(db: Session, usuario_id: int):
    return (
        db.query(Usuario)
        .filter(Usuario.id_usuario == usuario_id)
        .first()
    )

def create_usuario(
    db: Session,
    usuario: UsuarioCreate
):
    nuevo_usuario = Usuario(
        nombre=usuario.nombre,
        correo=usuario.correo,
        password=hash_password(usuario.password)
    )

    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)

    return nuevo_usuario