from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.crud.crud_detalles import (
    get_grupo_materia_detalle,
    get_grupos_materias_detalle
)
from app.crud.crud_grupo_materia import (
    create_grupo_materia,
    delete_grupo_materia,
    update_grupo_materia
)
from app.database import get_db
from app.schemas.detalles import GrupoMateriaDetalleResponse
from app.schemas.grupo_materia import GrupoMateriaCreate, GrupoMateriaUpdate


router = APIRouter(
    prefix="/grupos-materias",
    tags=["Grupos materias"]
)


@router.get(
    "/",
    response_model=list[GrupoMateriaDetalleResponse]
)
def listar_grupos_materias(
    grupo_id: Optional[int] = None,
    docente_id: Optional[int] = None,
    materia_id: Optional[int] = None,
    periodo_id: Optional[int] = None,
    db: Session = Depends(get_db)
):
    return get_grupos_materias_detalle(
        db,
        grupo_id=grupo_id,
        docente_id=docente_id,
        materia_id=materia_id,
        periodo_id=periodo_id
    )


@router.get(
    "/{grupo_materia_id}",
    response_model=GrupoMateriaDetalleResponse
)
def obtener_grupo_materia(
    grupo_materia_id: int,
    db: Session = Depends(get_db)
):
    grupo_materia = get_grupo_materia_detalle(db, grupo_materia_id)

    if not grupo_materia:
        raise HTTPException(
            status_code=404,
            detail="Grupo materia no encontrado"
        )

    return grupo_materia


@router.post(
    "/",
    response_model=GrupoMateriaDetalleResponse
)
def crear_grupo_materia(
    grupo_materia: GrupoMateriaCreate,
    db: Session = Depends(get_db)
):
    nuevo_grupo_materia = create_grupo_materia(db, grupo_materia)

    return get_grupo_materia_detalle(db, nuevo_grupo_materia.id_grupo_materia)


@router.patch(
    "/{grupo_materia_id}",
    response_model=GrupoMateriaDetalleResponse
)
def actualizar_grupo_materia(
    grupo_materia_id: int,
    grupo_materia: GrupoMateriaUpdate,
    db: Session = Depends(get_db)
):
    grupo_materia_actualizado = update_grupo_materia(
        db,
        grupo_materia_id,
        grupo_materia
    )

    if not grupo_materia_actualizado:
        raise HTTPException(
            status_code=404,
            detail="Grupo materia no encontrado"
        )

    return get_grupo_materia_detalle(db, grupo_materia_id)


@router.delete(
    "/{grupo_materia_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def eliminar_grupo_materia(
    grupo_materia_id: int,
    db: Session = Depends(get_db)
):
    eliminado = delete_grupo_materia(db, grupo_materia_id)

    if not eliminado:
        raise HTTPException(
            status_code=404,
            detail="Grupo materia no encontrado"
        )
