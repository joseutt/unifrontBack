from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.crud.crud_carga_academica import (
    create_carga_academica,
    delete_carga_academica,
    update_carga_academica
)
from app.crud.crud_detalles import (
    get_carga_academica_detalle,
    get_cargas_academicas_detalle
)
from app.database import get_db
from app.schemas.carga_academica import CargaAcademicaCreate, CargaAcademicaUpdate
from app.schemas.detalles import CargaAcademicaDetalleResponse


router = APIRouter(
    prefix="/cargas-academicas",
    tags=["Cargas academicas"]
)


@router.get(
    "/",
    response_model=list[CargaAcademicaDetalleResponse]
)
def listar_cargas_academicas(
    alumno_id: Optional[int] = None,
    grupo_id: Optional[int] = None,
    docente_id: Optional[int] = None,
    materia_id: Optional[int] = None,
    periodo_id: Optional[int] = None,
    estatus: Optional[str] = None,
    db: Session = Depends(get_db)
):
    return get_cargas_academicas_detalle(
        db,
        alumno_id=alumno_id,
        grupo_id=grupo_id,
        docente_id=docente_id,
        materia_id=materia_id,
        periodo_id=periodo_id,
        estatus=estatus
    )


@router.get(
    "/{carga_id}",
    response_model=CargaAcademicaDetalleResponse
)
def obtener_carga_academica(
    carga_id: int,
    db: Session = Depends(get_db)
):
    carga = get_carga_academica_detalle(db, carga_id)

    if not carga:
        raise HTTPException(
            status_code=404,
            detail="Carga academica no encontrada"
        )

    return carga


@router.post(
    "/",
    response_model=CargaAcademicaDetalleResponse
)
def crear_carga_academica(
    carga: CargaAcademicaCreate,
    db: Session = Depends(get_db)
):
    nueva_carga = create_carga_academica(db, carga)

    return get_carga_academica_detalle(db, nueva_carga.id_carga)


@router.patch(
    "/{carga_id}",
    response_model=CargaAcademicaDetalleResponse
)
def actualizar_carga_academica(
    carga_id: int,
    carga: CargaAcademicaUpdate,
    db: Session = Depends(get_db)
):
    carga_actualizada = update_carga_academica(db, carga_id, carga)

    if not carga_actualizada:
        raise HTTPException(
            status_code=404,
            detail="Carga academica no encontrada"
        )

    return get_carga_academica_detalle(db, carga_id)


@router.delete(
    "/{carga_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def eliminar_carga_academica(
    carga_id: int,
    db: Session = Depends(get_db)
):
    eliminada = delete_carga_academica(db, carga_id)

    if not eliminada:
        raise HTTPException(
            status_code=404,
            detail="Carga academica no encontrada"
        )
