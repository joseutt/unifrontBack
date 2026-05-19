from datetime import date
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.crud.crud_asistencia import (
    create_asistencia,
    delete_asistencia,
    update_asistencia
)
from app.crud.crud_detalles import (
    get_asistencia_detalle,
    get_asistencias_detalle
)
from app.database import get_db
from app.schemas.asistencia import AsistenciaCreate, AsistenciaUpdate
from app.schemas.detalles import AsistenciaDetalleResponse


router = APIRouter(
    prefix="/asistencias",
    tags=["Asistencias"]
)


@router.get(
    "/",
    response_model=list[AsistenciaDetalleResponse]
)
def listar_asistencias(
    alumno_id: Optional[int] = None,
    grupo_id: Optional[int] = None,
    materia_id: Optional[int] = None,
    periodo_id: Optional[int] = None,
    fecha_inicio: Optional[date] = None,
    fecha_fin: Optional[date] = None,
    db: Session = Depends(get_db)
):
    return get_asistencias_detalle(
        db,
        alumno_id=alumno_id,
        grupo_id=grupo_id,
        materia_id=materia_id,
        periodo_id=periodo_id,
        fecha_inicio=fecha_inicio,
        fecha_fin=fecha_fin
    )


@router.get(
    "/{asistencia_id}",
    response_model=AsistenciaDetalleResponse
)
def obtener_asistencia(
    asistencia_id: int,
    db: Session = Depends(get_db)
):
    asistencia = get_asistencia_detalle(db, asistencia_id)

    if not asistencia:
        raise HTTPException(
            status_code=404,
            detail="Asistencia no encontrada"
        )

    return asistencia


@router.post(
    "/",
    response_model=AsistenciaDetalleResponse
)
def crear_asistencia(
    asistencia: AsistenciaCreate,
    db: Session = Depends(get_db)
):
    nueva_asistencia = create_asistencia(db, asistencia)

    return get_asistencia_detalle(db, nueva_asistencia.id_asistencia)


@router.patch(
    "/{asistencia_id}",
    response_model=AsistenciaDetalleResponse
)
def actualizar_asistencia(
    asistencia_id: int,
    asistencia: AsistenciaUpdate,
    db: Session = Depends(get_db)
):
    asistencia_actualizada = update_asistencia(db, asistencia_id, asistencia)

    if not asistencia_actualizada:
        raise HTTPException(
            status_code=404,
            detail="Asistencia no encontrada"
        )

    return get_asistencia_detalle(db, asistencia_id)


@router.delete(
    "/{asistencia_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def eliminar_asistencia(
    asistencia_id: int,
    db: Session = Depends(get_db)
):
    eliminada = delete_asistencia(db, asistencia_id)

    if not eliminada:
        raise HTTPException(
            status_code=404,
            detail="Asistencia no encontrada"
        )
