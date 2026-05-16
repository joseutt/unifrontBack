from sqlalchemy.orm import Session

from app.models.docente import Docente

from app.schemas.docente import DocenteCreate

def get_docentes(db: Session):
    return db.query(Docente).all()

def create_docente(
    db: Session,
    docente: DocenteCreate
):
    nuevo_docente = Docente(
        **docente.model_dump()
    )

    db.add(nuevo_docente)

    db.commit()

    db.refresh(nuevo_docente)

    return nuevo_docente