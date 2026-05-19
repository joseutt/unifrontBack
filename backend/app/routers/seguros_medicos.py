from app.crud.crud_seguro_medico import (
    create_seguro_medico,
    delete_seguro_medico,
    get_seguro_medico,
    get_seguros_medicos,
    update_seguro_medico
)
from app.routers._crud_router import create_crud_router
from app.schemas.seguro_medico import (
    SeguroMedicoCreate,
    SeguroMedicoResponse,
    SeguroMedicoUpdate
)


router = create_crud_router(
    prefix="/seguros-medicos",
    tags=["Seguros medicos"],
    response_schema=SeguroMedicoResponse,
    create_schema=SeguroMedicoCreate,
    update_schema=SeguroMedicoUpdate,
    get_all=get_seguros_medicos,
    get_one=get_seguro_medico,
    create_one=create_seguro_medico,
    update_one=update_seguro_medico,
    delete_one=delete_seguro_medico,
    not_found_detail="Seguro medico no encontrado"
)
