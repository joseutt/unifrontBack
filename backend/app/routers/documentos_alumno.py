from app.crud.crud_documento_alumno import (
    create_documento_alumno,
    delete_documento_alumno,
    get_documento_alumno,
    get_documentos_alumno,
    update_documento_alumno
)
from app.routers._crud_router import create_crud_router
from app.schemas.documento_alumno import (
    DocumentoAlumnoCreate,
    DocumentoAlumnoResponse,
    DocumentoAlumnoUpdate
)


router = create_crud_router(
    prefix="/documentos-alumno",
    tags=["Documentos alumno"],
    response_schema=DocumentoAlumnoResponse,
    create_schema=DocumentoAlumnoCreate,
    update_schema=DocumentoAlumnoUpdate,
    get_all=get_documentos_alumno,
    get_one=get_documento_alumno,
    create_one=create_documento_alumno,
    update_one=update_documento_alumno,
    delete_one=delete_documento_alumno,
    not_found_detail="Documento de alumno no encontrado"
)
