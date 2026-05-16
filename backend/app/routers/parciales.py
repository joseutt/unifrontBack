from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from app.database import SessionLocal

from app.schemas.parcial import (
    ParcialCreate,
    ParcialResponse
)

from app.crud.crud_parcial import (
    get_parciales,
    create_parcial
)

from app.database import get_db

router = APIRouter(
    prefix="/parciales",
    tags=["Parciales"]
)



@router.get(
    "/",
    response_model=list[ParcialResponse]
)
def listar_parciales(
    db: Session = Depends(get_db)
):
    return get_parciales(db)

@router.post(
    "/",
    response_model=ParcialResponse
)
def crear_parcial(
    parcial: ParcialCreate,
    db: Session = Depends(get_db)
):
    return create_parcial(
        db,
        parcial
    )