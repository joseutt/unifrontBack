from app.crud.crud_procedencia_academica import (
    create_procedencia_academica,
    delete_procedencia_academica,
    get_procedencia_academica,
    get_procedencias_academicas,
    update_procedencia_academica
)
from app.routers._crud_router import create_crud_router
from app.schemas.procedencia_academica import (
    ProcedenciaAcademicaCreate,
    ProcedenciaAcademicaResponse,
    ProcedenciaAcademicaUpdate
)


router = create_crud_router(
    prefix="/procedencias-academicas",
    tags=["Procedencias academicas"],
    response_schema=ProcedenciaAcademicaResponse,
    create_schema=ProcedenciaAcademicaCreate,
    update_schema=ProcedenciaAcademicaUpdate,
    get_all=get_procedencias_academicas,
    get_one=get_procedencia_academica,
    create_one=create_procedencia_academica,
    update_one=update_procedencia_academica,
    delete_one=delete_procedencia_academica,
    not_found_detail="Procedencia academica no encontrada"
)
