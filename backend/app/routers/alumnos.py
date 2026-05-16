from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status
)

from sqlalchemy.orm import Session

from app.schemas.alumno import (
    AlumnoCreate,
    AlumnoResponse,
    AlumnoUpdate
)

from app.crud.crud_alumno import (
    get_alumnos,
    get_alumno,
    create_alumno,
    update_alumno,
    delete_alumno
)

from app.database import get_db

router = APIRouter(
    prefix="/alumnos",
    tags=["Alumnos"]
)




@router.get(
    "/",
    response_model=list[AlumnoResponse]
)
def listar_alumnos(
    db: Session = Depends(get_db)
):
    return get_alumnos(db)


@router.get(
    "/{alumno_id}",
    response_model=AlumnoResponse
)
def obtener_alumno(
    alumno_id: int,
    db: Session = Depends(get_db)
):

    alumno = get_alumno(
        db,
        alumno_id
    )

    if not alumno:
        raise HTTPException(
            status_code=404,
            detail="Alumno no encontrado"
        )

    return alumno


@router.post(
    "/",
    response_model=AlumnoResponse
)
def crear_alumno(
    alumno: AlumnoCreate,
    db: Session = Depends(get_db)
):
    return create_alumno(
        db,
        alumno
    )


@router.patch(
    "/{alumno_id}",
    response_model=AlumnoResponse
)
def actualizar_alumno(
    alumno_id: int,
    alumno: AlumnoUpdate,
    db: Session = Depends(get_db)
):

    alumno_actualizado = update_alumno(
        db,
        alumno_id,
        alumno
    )

    if not alumno_actualizado:
        raise HTTPException(
            status_code=404,
            detail="Alumno no encontrado"
        )

    return alumno_actualizado


@router.delete(
    "/{alumno_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def eliminar_alumno(
    alumno_id: int,
    db: Session = Depends(get_db)
):

    eliminado = delete_alumno(
        db,
        alumno_id
    )

    if not eliminado:
        raise HTTPException(
            status_code=404,
            detail="Alumno no encontrado"
        )
