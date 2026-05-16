from sqlalchemy.orm import Session

from app.models.titulacion import Titulacion

from app.schemas.titulacion import (
    TitulacionCreate
)

def get_titulaciones(db: Session):
    return db.query(Titulacion).all()

def create_titulacion(
    db: Session,
    titulacion: TitulacionCreate
):
    nueva_titulacion = Titulacion(
        **titulacion.model_dump()
    )

    db.add(nueva_titulacion)

    db.commit()

    db.refresh(nueva_titulacion)

    return nueva_titulacion