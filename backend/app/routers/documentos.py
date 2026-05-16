from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from app.database import get_db
from app.crud.crud_alumno import get_alumno
from app.services.document_service import generar_constancia
from app.database import get_db

router = APIRouter(
    prefix="/documentos",
    tags=["Documentos"]
)

@router.get("/constancia/{alumno_id}")
def generar_pdf(
    alumno_id: int,
    db: Session = Depends(get_db)
):

    alumno = get_alumno(db, alumno_id)

    ruta = generar_constancia(alumno)

    return FileResponse(
        path=ruta,
        media_type="application/pdf",
        filename="constancia.pdf"
    )