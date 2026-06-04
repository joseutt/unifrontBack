from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.crud.crud_kardex import get_kardex_by_matricula
from app.database import get_db

# Nota: sin control de roles porque tu petición no lo especifica.

router = APIRouter(prefix="/kardex", tags=["Kardex"])

from app.schemas.kardex import KardexResponse

@router.get("", response_model=KardexResponse)
def obtener_kardex(
    matricula: str = Query(..., min_length=1),
    db: Session = Depends(get_db),
):
    kardex = get_kardex_by_matricula(db, matricula=matricula)

    if not kardex:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Alumno no encontrado")

    return kardex

