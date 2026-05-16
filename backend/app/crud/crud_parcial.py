from sqlalchemy.orm import Session

from app.models.parcial import Parcial

from app.schemas.parcial import ParcialCreate

def get_parciales(db: Session):
    return db.query(Parcial).all()

def create_parcial(
    db: Session,
    parcial: ParcialCreate
):
    nuevo_parcial = Parcial(
        **parcial.model_dump()
    )

    db.add(nuevo_parcial)

    db.commit()

    db.refresh(nuevo_parcial)

    return nuevo_parcial