from app.crud.crud_historial_academico import (
    create_historial_academico,
    delete_historial_academico,
    get_historial_academico,
    get_historiales_academicos,
    update_historial_academico
)
from app.routers._crud_router import create_crud_router
from app.schemas.historial_academico import (
    HistorialAcademicoCreate,
    HistorialAcademicoResponse,
    HistorialAcademicoUpdate
)


router = create_crud_router(
    prefix="/historiales-academicos",
    tags=["Historiales academicos"],
    response_schema=HistorialAcademicoResponse,
    create_schema=HistorialAcademicoCreate,
    update_schema=HistorialAcademicoUpdate,
    get_all=get_historiales_academicos,
    get_one=get_historial_academico,
    create_one=create_historial_academico,
    update_one=update_historial_academico,
    delete_one=delete_historial_academico,
    not_found_detail="Historial academico no encontrado"
)
