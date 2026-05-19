from app.crud.crud_recepcion_documento import (
    create_recepcion_documento,
    delete_recepcion_documento,
    get_recepcion_documento,
    get_recepciones_documento,
    update_recepcion_documento
)
from app.routers._crud_router import create_crud_router
from app.schemas.recepcion_documento import (
    RecepcionDocumentoCreate,
    RecepcionDocumentoResponse,
    RecepcionDocumentoUpdate
)


router = create_crud_router(
    prefix="/recepciones-documento",
    tags=["Recepciones documento"],
    response_schema=RecepcionDocumentoResponse,
    create_schema=RecepcionDocumentoCreate,
    update_schema=RecepcionDocumentoUpdate,
    get_all=get_recepciones_documento,
    get_one=get_recepcion_documento,
    create_one=create_recepcion_documento,
    update_one=update_recepcion_documento,
    delete_one=delete_recepcion_documento,
    not_found_detail="Recepcion de documento no encontrada"
)
