from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from app.database import SessionLocal

from app.schemas.periodo import (
    PeriodoCreate,
    PeriodoResponse
)

from app.crud.crud_periodo import (
    get_periodos,
    create_periodo
)

from app.database import get_db

router = APIRouter(
    prefix="/periodos",
    tags=["Periodos"]
)



@router.get(
    "/",
    response_model=list[PeriodoResponse]
)
def listar_periodos(
    db: Session = Depends(get_db)
):
    return get_periodos(db)

@router.post(
    "/",
    response_model=PeriodoResponse
)
def crear_periodo(
    periodo: PeriodoCreate,
    db: Session = Depends(get_db)
):
    return create_periodo(
        db,
        periodo
    )