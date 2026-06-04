from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.crud.crud_kardex import buscar_alumnos_kardex, get_kardex_by_query
from app.database import get_db

# Nota: sin control de roles porque tu petición no lo especifica.

router = APIRouter(prefix="/kardex", tags=["Kardex"])

from app.schemas.kardex import KardexAlumnoBusqueda, KardexResponse


@router.get("/buscar", response_model=list[KardexAlumnoBusqueda])
def buscar_alumnos(
    q: str = Query(..., min_length=2),
    db: Session = Depends(get_db),
):
    return buscar_alumnos_kardex(db, query=q)

@router.get("", response_model=KardexResponse)
def obtener_kardex(
    matricula: str | None = Query(None, min_length=1),
    q: str | None = Query(None, min_length=1),
    db: Session = Depends(get_db),
):
    termino = matricula or q or ""
    kardex = get_kardex_by_query(db, query=termino)

    if not kardex:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Alumno no encontrado")

    return kardex

