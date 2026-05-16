from fastapi import (
    APIRouter,
    Depends
)

from app.database import get_db

from sqlalchemy.orm import Session

from app.database import SessionLocal

from app.schemas.calificacion import (
    CalificacionCreate,
    CalificacionResponse
)

from app.crud.crud_calificacion import (
    get_calificaciones,
    create_calificacion
)

router = APIRouter(
    prefix="/calificaciones",
    tags=["Calificaciones"]
)



@router.get(
    "/",
    response_model=list[CalificacionResponse]
)
def listar_calificaciones(
    db: Session = Depends(get_db)
):
    return get_calificaciones(db)

@router.post(
    "/",
    response_model=CalificacionResponse
)
def crear_calificacion(
    calificacion: CalificacionCreate,
    db: Session = Depends(get_db)
):
    return create_calificacion(
        db,
        calificacion
    )