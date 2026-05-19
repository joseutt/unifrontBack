from app.crud.crud_contacto_emergencia import (
    create_contacto_emergencia,
    delete_contacto_emergencia,
    get_contacto_emergencia,
    get_contactos_emergencia,
    update_contacto_emergencia
)
from app.routers._crud_router import create_crud_router
from app.schemas.contacto_emergencia import (
    ContactoEmergenciaCreate,
    ContactoEmergenciaResponse,
    ContactoEmergenciaUpdate
)


router = create_crud_router(
    prefix="/contactos-emergencia",
    tags=["Contactos emergencia"],
    response_schema=ContactoEmergenciaResponse,
    create_schema=ContactoEmergenciaCreate,
    update_schema=ContactoEmergenciaUpdate,
    get_all=get_contactos_emergencia,
    get_one=get_contacto_emergencia,
    create_one=create_contacto_emergencia,
    update_one=update_contacto_emergencia,
    delete_one=delete_contacto_emergencia,
    not_found_detail="Contacto de emergencia no encontrado"
)
