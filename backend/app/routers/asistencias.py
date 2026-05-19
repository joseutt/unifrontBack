from app.crud.crud_asistencia import (
    create_asistencia,
    delete_asistencia,
    get_asistencia,
    get_asistencias,
    update_asistencia
)
from app.routers._crud_router import create_crud_router
from app.schemas.asistencia import (
    AsistenciaCreate,
    AsistenciaResponse,
    AsistenciaUpdate
)


router = create_crud_router(
    prefix="/asistencias",
    tags=["Asistencias"],
    response_schema=AsistenciaResponse,
    create_schema=AsistenciaCreate,
    update_schema=AsistenciaUpdate,
    get_all=get_asistencias,
    get_one=get_asistencia,
    create_one=create_asistencia,
    update_one=update_asistencia,
    delete_one=delete_asistencia,
    not_found_detail="Asistencia no encontrada"
)
