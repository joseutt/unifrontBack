from app.crud.crud_grupo_materia import (
    create_grupo_materia,
    delete_grupo_materia,
    get_grupo_materia,
    get_grupos_materias,
    update_grupo_materia
)
from app.routers._crud_router import create_crud_router
from app.schemas.grupo_materia import (
    GrupoMateriaCreate,
    GrupoMateriaResponse,
    GrupoMateriaUpdate
)


router = create_crud_router(
    prefix="/grupos-materias",
    tags=["Grupos materias"],
    response_schema=GrupoMateriaResponse,
    create_schema=GrupoMateriaCreate,
    update_schema=GrupoMateriaUpdate,
    get_all=get_grupos_materias,
    get_one=get_grupo_materia,
    create_one=create_grupo_materia,
    update_one=update_grupo_materia,
    delete_one=delete_grupo_materia,
    not_found_detail="Grupo materia no encontrado"
)
