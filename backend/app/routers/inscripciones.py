from app.crud.crud_inscripcion import (
    create_inscripcion,
    delete_inscripcion,
    get_inscripcion,
    get_inscripciones,
    update_inscripcion
)
from app.routers._crud_router import create_crud_router
from app.schemas.inscripcion import (
    InscripcionCreate,
    InscripcionResponse,
    InscripcionUpdate
)


router = create_crud_router(
    prefix="/inscripciones",
    tags=["Inscripciones"],
    response_schema=InscripcionResponse,
    create_schema=InscripcionCreate,
    update_schema=InscripcionUpdate,
    get_all=get_inscripciones,
    get_one=get_inscripcion,
    create_one=create_inscripcion,
    update_one=update_inscripcion,
    delete_one=delete_inscripcion,
    not_found_detail="Inscripcion no encontrada"
)
