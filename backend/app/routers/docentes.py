from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from app.database import SessionLocal

from app.schemas.docente import (
    DocenteCreate,
    DocenteResponse
)

from app.crud.crud_docente import (
    get_docentes,
    create_docente
)

from app.database import get_db

router = APIRouter(
    prefix="/docentes",
    tags=["Docentes"]
)



@router.get(
    "/",
    response_model=list[DocenteResponse]
)
def listar_docentes(
    db: Session = Depends(get_db)
):
    return get_docentes(db)

@router.post(
    "/",
    response_model=DocenteResponse
)
def crear_docente(
    docente: DocenteCreate,
    db: Session = Depends(get_db)
):
    return create_docente(
        db,
        docente
    )