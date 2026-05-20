from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, joinedload

from app.core.security import get_current_user
from app.crud.crud_calificacion import (
    create_calificacion,
    delete_calificacion,
    get_calificacion,
    update_calificacion
)
from app.crud.crud_detalles import (
    get_calificaciones_detalle,
    get_grupo_materia_detalle,
    get_grupos_materias_detalle
)
from app.database import get_db
from app.models.alumno import Alumno
from app.models.calificacion import Calificacion
from app.models.carga_academica import CargaAcademica
from app.models.docente import Docente
from app.models.grupo_materia import GrupoMateria
from app.models.parcial import Parcial
from app.models.usuario import Usuario
from app.schemas.calificacion import (
    CalificacionCreate,
    CalificacionUpdate,
    CapturaCalificacionesBatch,
    CapturaCalificacionesResponse
)
from app.schemas.detalles import (
    CalificacionDetalleResponse,
    GrupoMateriaDetalleResponse
)


router = APIRouter(
    prefix="/calificaciones",
    tags=["Calificaciones"]
)


def _nombre_usuario(usuario):
    if not usuario:
        return None

    partes = [
        usuario.nombre,
        usuario.apellido_paterno,
        usuario.apellido_materno
    ]

    return " ".join(parte for parte in partes if parte)


def _alumno_detalle(alumno):
    if not alumno:
        return None

    return {
        "id_alumno": alumno.id_alumno,
        "matricula": alumno.matricula,
        "numero_control": alumno.numero_control,
        "nombre": _nombre_usuario(alumno.usuario)
    }


def _parcial_detalle(parcial):
    return {
        "id_parcial": parcial.id_parcial,
        "nombre": parcial.nombre,
        "porcentaje": (
            float(parcial.porcentaje)
            if parcial.porcentaje is not None else None
        )
    }


def _get_docente_actual(db: Session, usuario: Usuario):
    docente = (
        db.query(Docente)
        .filter(
            Docente.id_usuario == usuario.id_usuario,
            Docente.estado.is_(True)
        )
        .first()
    )

    if not docente:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="El usuario actual no tiene un perfil docente activo"
        )

    return docente


def _validar_grupo_docente(
    db: Session,
    grupo_materia_id: int,
    docente_id: int
):
    grupo_materia = (
        db.query(GrupoMateria)
        .filter(
            GrupoMateria.id_grupo_materia == grupo_materia_id,
            GrupoMateria.id_docente == docente_id
        )
        .first()
    )

    if not grupo_materia:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="El grupo no esta asignado al docente actual"
        )

    return grupo_materia


def _build_captura_response(db: Session, grupo_materia_id: int):
    grupo_materia = get_grupo_materia_detalle(db, grupo_materia_id)
    parciales = db.query(Parcial).order_by(Parcial.id_parcial).all()
    cargas = (
        db.query(CargaAcademica)
        .options(
            joinedload(CargaAcademica.alumno)
            .joinedload(Alumno.usuario)
        )
        .filter(CargaAcademica.id_grupo_materia == grupo_materia_id)
        .order_by(CargaAcademica.id_alumno)
        .all()
    )

    cargas_ids = [carga.id_carga for carga in cargas]
    calificaciones = []

    if cargas_ids:
        calificaciones = (
            db.query(Calificacion)
            .filter(Calificacion.id_carga.in_(cargas_ids))
            .all()
        )

    calificaciones_por_celda = {
        (calificacion.id_carga, calificacion.id_parcial): calificacion
        for calificacion in calificaciones
    }

    def _calificacion_celda(carga, parcial):
        calificacion = calificaciones_por_celda.get(
            (carga.id_carga, parcial.id_parcial)
        )

        return {
            "id_calificacion": (
                calificacion.id_calificacion
                if calificacion else None
            ),
            "id_carga": carga.id_carga,
            "id_parcial": parcial.id_parcial,
            "calificacion": (
                float(calificacion.calificacion)
                if calificacion
                and calificacion.calificacion is not None
                else None
            )
        }

    return {
        "grupo_materia": grupo_materia,
        "parciales": [
            _parcial_detalle(parcial)
            for parcial in parciales
        ],
        "alumnos": [
            {
                "id_carga": carga.id_carga,
                "estatus": carga.estatus,
                "alumno": _alumno_detalle(carga.alumno),
                "calificaciones": [
                    _calificacion_celda(carga, parcial)
                    for parcial in parciales
                ]
            }
            for carga in cargas
        ]
    }


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
    "/captura/grupos",
    response_model=list[GrupoMateriaDetalleResponse]
)
def listar_grupos_captura(
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)
):
    docente = _get_docente_actual(db, usuario)

    return get_grupos_materias_detalle(
        db,
        docente_id=docente.id_docente
    )


@router.get(
    "/captura/grupos/{grupo_materia_id}",
    response_model=CapturaCalificacionesResponse
)
def obtener_captura_grupo(
    grupo_materia_id: int,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)
):
    docente = _get_docente_actual(db, usuario)
    _validar_grupo_docente(db, grupo_materia_id, docente.id_docente)

    return _build_captura_response(db, grupo_materia_id)


@router.post(
    "/captura",
    response_model=CapturaCalificacionesResponse
)
def guardar_captura_calificaciones(
    captura: CapturaCalificacionesBatch,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)
):
    docente = _get_docente_actual(db, usuario)
    _validar_grupo_docente(
        db,
        captura.grupo_materia_id,
        docente.id_docente
    )

    cargas_validas = {
        id_carga
        for (id_carga,) in (
            db.query(CargaAcademica.id_carga)
            .filter(
                CargaAcademica.id_grupo_materia == captura.grupo_materia_id
            )
            .all()
        )
    }

    parciales_validos = {
        id_parcial
        for (id_parcial,) in db.query(Parcial.id_parcial).all()
    }

    for item in captura.calificaciones:
        if item.id_carga not in cargas_validas:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="La carga academica no pertenece al grupo asignado"
            )

        if item.id_parcial not in parciales_validos:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Parcial no encontrado"
            )

        calificacion = (
            db.query(Calificacion)
            .filter(
                Calificacion.id_carga == item.id_carga,
                Calificacion.id_parcial == item.id_parcial
            )
            .first()
        )

        if calificacion:
            calificacion.calificacion = item.calificacion
            calificacion.capturado_por = usuario.id_usuario
            continue

        if item.calificacion is None:
            continue

        db.add(
            Calificacion(
                id_carga=item.id_carga,
                id_parcial=item.id_parcial,
                calificacion=item.calificacion,
                capturado_por=usuario.id_usuario
            )
        )

    db.commit()

    return _build_captura_response(db, captura.grupo_materia_id)


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
