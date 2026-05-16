from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.schemas.usuario import (
    UsuarioCreate,
    UsuarioResponse
)

from app.crud.crud_usuario import (
    get_usuarios,
    create_usuario
)

from app.database import get_db

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get(
    "/",
    response_model=list[UsuarioResponse]
)
def listar_usuarios(
    db: Session = Depends(get_db)
):
    return get_usuarios(db)

@router.post(
    "/",
    response_model=UsuarioResponse
)
def crear_usuario(
    usuario: UsuarioCreate,
    db: Session = Depends(get_db)
):
    return create_usuario(db, usuario)