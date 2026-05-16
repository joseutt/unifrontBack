from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from app.database import SessionLocal

from app.schemas.titulacion import (
    TitulacionCreate,
    TitulacionResponse
)

from app.crud.crud_titulacion import (
    get_titulaciones,
    create_titulacion
)

from app.database import get_db

router = APIRouter(
    prefix="/titulaciones",
    tags=["Titulacion"]
)



@router.get(
    "/",
    response_model=list[TitulacionResponse]
)
def listar_titulaciones(
    db: Session = Depends(get_db)
):
    return get_titulaciones(db)

@router.post(
    "/",
    response_model=TitulacionResponse
)
def crear_titulacion(
    titulacion: TitulacionCreate,
    db: Session = Depends(get_db)
):
    return create_titulacion(
        db,
        titulacion
    )