from sqlalchemy.orm import Session

from app.models.calificacion import Calificacion

from app.schemas.calificacion import (
    CalificacionCreate
)

def get_calificaciones(db: Session):
    return db.query(Calificacion).all()

def create_calificacion(
    db: Session,
    calificacion: CalificacionCreate
):
    nueva_calificacion = Calificacion(
        **calificacion.model_dump()
    )

    db.add(nueva_calificacion)

    db.commit()

    db.refresh(nueva_calificacion)

    return nueva_calificacion