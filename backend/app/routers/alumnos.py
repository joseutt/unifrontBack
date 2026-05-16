from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.core.security import (
    get_current_user
)

from app.database import SessionLocal

from app.schemas.alumno import (
    AlumnoCreate,
    AlumnoResponse,
    AlumnoUpdate
)

from app.crud.crud_alumno import (
    get_alumnos,
    get_alumno_by_id,
    create_alumno,
    update_alumno
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

    alumno = get_alumno_by_id(
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