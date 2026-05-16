from sqlalchemy.orm import Session

from app.models.periodo import Periodo

from app.schemas.periodo import PeriodoCreate

def get_periodos(db: Session):
    return db.query(Periodo).all()

def create_periodo(
    db: Session,
    periodo: PeriodoCreate
):
    nuevo_periodo = Periodo(
        **periodo.model_dump()
    )

    db.add(nuevo_periodo)

    db.commit()

    db.refresh(nuevo_periodo)

    return nuevo_periodo