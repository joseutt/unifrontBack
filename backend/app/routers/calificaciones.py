from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status
)

from app.database import get_db

from sqlalchemy.orm import Session

from app.schemas.calificacion import (
    CalificacionCreate,
    CalificacionResponse,
    CalificacionUpdate
)

from app.crud.crud_calificacion import (
    get_calificaciones,
    get_calificacion,
    create_calificacion,
    update_calificacion,
    delete_calificacion
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

@router.get(
    "/{calificacion_id}",
    response_model=CalificacionResponse
)
def obtener_calificacion(
    calificacion_id: int,
    db: Session = Depends(get_db)
):
    calificacion = get_calificacion(db, calificacion_id)

    if not calificacion:
        raise HTTPException(
            status_code=404,
            detail="Calificacion no encontrada"
        )

    return calificacion

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

@router.patch(
    "/{calificacion_id}",
    response_model=CalificacionResponse
)
def actualizar_calificacion(
    calificacion_id: int,
    calificacion: CalificacionUpdate,
    db: Session = Depends(get_db)
):
    calificacion_actualizada = update_calificacion(
        db,
        calificacion_id,
        calificacion
    )

    if not calificacion_actualizada:
        raise HTTPException(
            status_code=404,
            detail="Calificacion no encontrada"
        )

    return calificacion_actualizada

@router.delete(
    "/{calificacion_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def eliminar_calificacion(
    calificacion_id: int,
    db: Session = Depends(get_db)
):
    eliminada = delete_calificacion(db, calificacion_id)

    if not eliminada:
        raise HTTPException(
            status_code=404,
            detail="Calificacion no encontrada"
        )
