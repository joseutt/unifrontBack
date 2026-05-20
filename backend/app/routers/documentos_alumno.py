import shutil
from pathlib import Path
from typing import Optional
from uuid import uuid4

from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile, status
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


STATIC_DIR = Path(__file__).resolve().parents[1] / "static"
DOCUMENTOS_DIR = STATIC_DIR / "documentos-alumno"
EXTENSIONES_PERMITIDAS = {".pdf", ".png", ".jpg", ".jpeg", ".webp"}

router = APIRouter(
    prefix="/documentos-alumno",
    tags=["Documentos alumno"]
)


def _detalle_documento(db: Session, documento_id: int):
    return next(
        item for item in get_documentos_alumno_detalle(db)
        if item["id_documento"] == documento_id
    )


def _eliminar_archivo_estatico(ruta_archivo: Optional[str]):
    if not ruta_archivo or not ruta_archivo.startswith("/static/documentos-alumno/"):
        return

    archivo = (STATIC_DIR / ruta_archivo.removeprefix("/static/")).resolve()
    raiz_documentos = DOCUMENTOS_DIR.resolve()

    try:
        archivo.relative_to(raiz_documentos)
    except ValueError:
        return

    if archivo.is_file():
        archivo.unlink()


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

    return _detalle_documento(db, nuevo_documento.id_documento)


@router.post(
    "/upload",
    response_model=DocumentoAlumnoDetalleResponse
)
def subir_documento_alumno(
    id_alumno: int = Form(...),
    id_tipo_documento: int = Form(...),
    validado: bool = Form(True),
    observaciones: Optional[str] = Form(None),
    archivo: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    nombre_original = archivo.filename or "documento"
    extension = Path(nombre_original).suffix.lower()

    if extension not in EXTENSIONES_PERMITIDAS:
        raise HTTPException(
            status_code=400,
            detail="Solo se permiten archivos PDF o imagenes"
        )

    carpeta_alumno = DOCUMENTOS_DIR / str(id_alumno)
    carpeta_alumno.mkdir(parents=True, exist_ok=True)

    nombre_seguro = f"{uuid4().hex}{extension}"
    ruta_destino = carpeta_alumno / nombre_seguro

    with ruta_destino.open("wb") as destino:
        shutil.copyfileobj(archivo.file, destino)

    nuevo_documento = create_documento_alumno(
        db,
        DocumentoAlumnoCreate(
            id_alumno=id_alumno,
            id_tipo_documento=id_tipo_documento,
            nombre_archivo=nombre_original,
            ruta_archivo=f"/static/documentos-alumno/{id_alumno}/{nombre_seguro}",
            validado=validado,
            observaciones=observaciones
        )
    )

    return _detalle_documento(db, nuevo_documento.id_documento)


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
    documento = get_documento_alumno(db, documento_id)

    if not documento:
        raise HTTPException(
            status_code=404,
            detail="Documento de alumno no encontrado"
        )

    _eliminar_archivo_estatico(documento.ruta_archivo)
    delete_documento_alumno(db, documento_id)
