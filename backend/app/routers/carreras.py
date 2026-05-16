from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal

from app.schemas.carrera import (
    CarreraCreate,
    CarreraResponse
)

from app.crud.crud_carrera import (
    get_carreras,
    create_carrera
)

from app.database import get_db

router = APIRouter(
    prefix="/carreras",
    tags=["Carreras"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get(
    "/",
    response_model=list[CarreraResponse]
)
def listar_carreras(
    db: Session = Depends(get_db)
):
    return get_carreras(db)

@router.post(
    "/",
    response_model=CarreraResponse
)
def crear_carrera(
    carrera: CarreraCreate,
    db: Session = Depends(get_db)
):
    return create_carrera(db, carrera)