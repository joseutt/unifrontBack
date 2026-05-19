from app.crud.crud_practica_profesional import (
    create_practica_profesional,
    delete_practica_profesional,
    get_practica_profesional,
    get_practicas_profesionales,
    update_practica_profesional
)
from app.routers._crud_router import create_crud_router
from app.schemas.practica_profesional import (
    PracticaProfesionalCreate,
    PracticaProfesionalResponse,
    PracticaProfesionalUpdate
)


router = create_crud_router(
    prefix="/practicas-profesionales",
    tags=["Practicas profesionales"],
    response_schema=PracticaProfesionalResponse,
    create_schema=PracticaProfesionalCreate,
    update_schema=PracticaProfesionalUpdate,
    get_all=get_practicas_profesionales,
    get_one=get_practica_profesional,
    create_one=create_practica_profesional,
    update_one=update_practica_profesional,
    delete_one=delete_practica_profesional,
    not_found_detail="Practica profesional no encontrada"
)
