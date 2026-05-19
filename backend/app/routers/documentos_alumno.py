from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.crud.crud_detalles import get_documentos_alumno_detalle
from app.crud.crud_documento_alumno import (
    create_documento_alumno,
    delete_documento_alumno,
    get_documento_alumno,
    update_documento_alumno
)
from app.database import get_db
from app.schemas.detalles import DocumentoAlumnoDetalleResponse
from app.schemas.documento_alumno import DocumentoAlumnoCreate, DocumentoAlumnoUpdate


router = APIRouter(
    prefix="/documentos-alumno",
    tags=["Documentos alumno"]
)


@router.get(
    "/",
    response_model=list[DocumentoAlumnoDetalleResponse]
)
def listar_documentos_alumno(
    alumno_id: Optional[int] = None,
    tipo_documento_id: Optional[int] = None,
    validado: Optional[bool] = None,
    db: Session = Depends(get_db)
):
    return get_documentos_alumno_detalle(
        db,
        alumno_id=alumno_id,
        tipo_documento_id=tipo_documento_id,
        validado=validado
    )


@router.get(
    "/{documento_id}",
    response_model=DocumentoAlumnoDetalleResponse
)
def obtener_documento_alumno(
    documento_id: int,
    db: Session = Depends(get_db)
):
    documento = next(
        (
            item for item in get_documentos_alumno_detalle(db)
            if item["id_documento"] == documento_id
        ),
        None
    )

    if not documento:
        raise HTTPException(
            status_code=404,
            detail="Documento de alumno no encontrado"
        )

    return documento


@router.post(
    "/",
    response_model=DocumentoAlumnoDetalleResponse
)
def crear_documento_alumno(
    documento: DocumentoAlumnoCreate,
    db: Session = Depends(get_db)
):
    nuevo_documento = create_documento_alumno(db, documento)

    return next(
        item for item in get_documentos_alumno_detalle(db)
        if item["id_documento"] == nuevo_documento.id_documento
    )


@router.patch(
    "/{documento_id}",
    response_model=DocumentoAlumnoDetalleResponse
)
def actualizar_documento_alumno(
    documento_id: int,
    documento: DocumentoAlumnoUpdate,
    db: Session = Depends(get_db)
):
    documento_actualizado = update_documento_alumno(db, documento_id, documento)

    if not documento_actualizado:
        raise HTTPException(
            status_code=404,
            detail="Documento de alumno no encontrado"
        )

    return next(
        item for item in get_documentos_alumno_detalle(db)
        if item["id_documento"] == documento_id
    )


@router.delete(
    "/{documento_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def eliminar_documento_alumno(
    documento_id: int,
    db: Session = Depends(get_db)
):
    if not get_documento_alumno(db, documento_id):
        raise HTTPException(
            status_code=404,
            detail="Documento de alumno no encontrado"
        )

    delete_documento_alumno(db, documento_id)
