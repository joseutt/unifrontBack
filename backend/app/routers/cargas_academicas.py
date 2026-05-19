from app.crud.crud_carga_academica import (
    create_carga_academica,
    delete_carga_academica,
    get_carga_academica,
    get_cargas_academicas,
    update_carga_academica
)
from app.routers._crud_router import create_crud_router
from app.schemas.carga_academica import (
    CargaAcademicaCreate,
    CargaAcademicaResponse,
    CargaAcademicaUpdate
)


router = create_crud_router(
    prefix="/cargas-academicas",
    tags=["Cargas academicas"],
    response_schema=CargaAcademicaResponse,
    create_schema=CargaAcademicaCreate,
    update_schema=CargaAcademicaUpdate,
    get_all=get_cargas_academicas,
    get_one=get_carga_academica,
    create_one=create_carga_academica,
    update_one=update_carga_academica,
    delete_one=delete_carga_academica,
    not_found_detail="Carga academica no encontrada"
)
