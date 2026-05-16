from sqlalchemy.orm import Session
from app.models.carrera import Carrera
from app.schemas.carrera import CarreraCreate

def get_carreras(db: Session):
    return db.query(Carrera).all()

def create_carrera(
    db: Session,
    carrera: CarreraCreate
):
    nueva_carrera = Carrera(
        **carrera.model_dump()
    )

    db.add(nueva_carrera)
    db.commit()
    db.refresh(nueva_carrera)

    return nueva_carrera