from sqlalchemy.orm import Session

from app.models.alumno import Alumno

from app.schemas.alumno import AlumnoCreate

def get_alumnos(db: Session):
    return db.query(Alumno).all()

def get_alumno(
    db: Session,
    alumno_id: int
):
    return (
        db.query(Alumno)
        .filter(
            Alumno.id_alumno == alumno_id
        )
        .first()
    )

def create_alumno(
    db: Session,
    alumno: AlumnoCreate
):
    nuevo_alumno = Alumno(
        **alumno.model_dump()
    )

    db.add(nuevo_alumno)

    db.commit()

    db.refresh(nuevo_alumno)

    return nuevo_alumno

def get_alumno_by_id(
    db: Session,
    alumno_id: int
):
    return (
        db.query(Alumno)
        .filter(Alumno.id == alumno_id)
        .first()
    )


def update_alumno(
    db: Session,
    alumno_id: int,
    alumno_data
):

    alumno = (
        db.query(Alumno)
        .filter(Alumno.id == alumno_id)
        .first()
    )

    if not alumno:
        return None

    update_data = alumno_data.dict(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(alumno, key, value)

    db.commit()
    db.refresh(alumno)

    return alumno