from app.crud.crud_servicio_social import (
    create_servicio_social,
    delete_servicio_social,
    get_servicio_social,
    get_servicios_sociales,
    update_servicio_social
)
from app.routers._crud_router import create_crud_router
from app.schemas.servicio_social import (
    ServicioSocialCreate,
    ServicioSocialResponse,
    ServicioSocialUpdate
)


router = create_crud_router(
    prefix="/servicios-sociales",
    tags=["Servicios sociales"],
    response_schema=ServicioSocialResponse,
    create_schema=ServicioSocialCreate,
    update_schema=ServicioSocialUpdate,
    get_all=get_servicios_sociales,
    get_one=get_servicio_social,
    create_one=create_servicio_social,
    update_one=update_servicio_social,
    delete_one=delete_servicio_social,
    not_found_detail="Servicio social no encontrado"
)
