from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.crud.crud_calificacion import (
    create_calificacion,
    delete_calificacion,
    get_calificacion,
    update_calificacion
)
from app.crud.crud_detalles import get_calificaciones_detalle
from app.database import get_db
from app.schemas.calificacion import CalificacionCreate, CalificacionUpdate
from app.schemas.detalles import CalificacionDetalleResponse


router = APIRouter(
    prefix="/calificaciones",
    tags=["Calificaciones"]
)


@router.get(
    "/",
    response_model=list[CalificacionDetalleResponse]
)
def listar_calificaciones(
    alumno_id: Optional[int] = None,
    materia_id: Optional[int] = None,
    grupo_id: Optional[int] = None,
    periodo_id: Optional[int] = None,
    parcial_id: Optional[int] = None,
    db: Session = Depends(get_db)
):
    return get_calificaciones_detalle(
        db,
        alumno_id=alumno_id,
        materia_id=materia_id,
        grupo_id=grupo_id,
        periodo_id=periodo_id,
        parcial_id=parcial_id
    )


@router.get(
    "/{calificacion_id}",
    response_model=CalificacionDetalleResponse
)
def obtener_calificacion(
    calificacion_id: int,
    db: Session = Depends(get_db)
):
    calificacion = next(
        (
            item for item in get_calificaciones_detalle(db)
            if item["id_calificacion"] == calificacion_id
        ),
        None
    )

    if not calificacion:
        raise HTTPException(
            status_code=404,
            detail="Calificacion no encontrada"
        )

    return calificacion


@router.post(
    "/",
    response_model=CalificacionDetalleResponse
)
def crear_calificacion(
    calificacion: CalificacionCreate,
    db: Session = Depends(get_db)
):
    nueva_calificacion = create_calificacion(db, calificacion)

    return next(
        item for item in get_calificaciones_detalle(db)
        if item["id_calificacion"] == nueva_calificacion.id_calificacion
    )


@router.patch(
    "/{calificacion_id}",
    response_model=CalificacionDetalleResponse
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

    return next(
        item for item in get_calificaciones_detalle(db)
        if item["id_calificacion"] == calificacion_id
    )


@router.delete(
    "/{calificacion_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def eliminar_calificacion(
    calificacion_id: int,
    db: Session = Depends(get_db)
):
    if not get_calificacion(db, calificacion_id):
        raise HTTPException(
            status_code=404,
            detail="Calificacion no encontrada"
        )

    delete_calificacion(db, calificacion_id)
