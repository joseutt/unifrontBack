from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status
)

from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.periodo import (
    PeriodoCreate,
    PeriodoResponse,
    PeriodoUpdate
)

from app.crud.crud_periodo import (
    get_periodos,
    get_periodo,
    create_periodo,
    update_periodo,
    delete_periodo
)

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

@router.get(
    "/{periodo_id}",
    response_model=PeriodoResponse
)
def obtener_periodo(
    periodo_id: int,
    db: Session = Depends(get_db)
):
    periodo = get_periodo(db, periodo_id)

    if not periodo:
        raise HTTPException(
            status_code=404,
            detail="Periodo no encontrado"
        )

    return periodo

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

@router.patch(
    "/{periodo_id}",
    response_model=PeriodoResponse
)
def actualizar_periodo(
    periodo_id: int,
    periodo: PeriodoUpdate,
    db: Session = Depends(get_db)
):
    periodo_actualizado = update_periodo(
        db,
        periodo_id,
        periodo
    )

    if not periodo_actualizado:
        raise HTTPException(
            status_code=404,
            detail="Periodo no encontrado"
        )

    return periodo_actualizado

@router.delete(
    "/{periodo_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def eliminar_periodo(
    periodo_id: int,
    db: Session = Depends(get_db)
):
    eliminado = delete_periodo(db, periodo_id)

    if not eliminado:
        raise HTTPException(
            status_code=404,
            detail="Periodo no encontrado"
        )
