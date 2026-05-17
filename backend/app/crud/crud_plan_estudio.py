from sqlalchemy.orm import Session
from app.models.plan_estudio import PlanEstudio
from app.models.plan_materia import PlanMateria
from sqlalchemy.orm import joinedload

from app.schemas.plan_estudio import (
    PlanEstudioCreate,
    PlanEstudioUpdate
)


def crear_plan_estudio(
    db: Session,
    plan_data: PlanEstudioCreate
):
    nuevo_plan = PlanEstudio(
        id_carrera=plan_data.id_carrera,
        nombre_plan=plan_data.nombre_plan,
        fecha_inicio=plan_data.fecha_inicio,
        fecha_fin=plan_data.fecha_fin,
        vigente=plan_data.vigente
    )

    db.add(nuevo_plan)
    db.commit()
    db.refresh(nuevo_plan)

    for materia in plan_data.materias:
        nueva_materia = PlanMateria(
            id_plan=nuevo_plan.id_plan,
            id_materia=materia.id_materia,
            id_cuatrimestre=materia.id_cuatrimestre,
            obligatoria=materia.obligatoria
        )

        db.add(nueva_materia)

    db.commit()
    db.refresh(nuevo_plan)

    return nuevo_plan


def obtener_planes(db: Session):
    return (
        db.query(PlanEstudio)
        .options(
            joinedload(PlanEstudio.carrera),

            joinedload(PlanEstudio.materias)
            .joinedload(PlanMateria.materia),

            joinedload(PlanEstudio.materias)
            .joinedload(PlanMateria.cuatrimestre)
        )
        .all()
    )


def obtener_plan_por_id(
    db: Session,
    id_plan: int
):
    return (
        db.query(PlanEstudio)
        .options(
            joinedload(PlanEstudio.materias)
            .joinedload(PlanMateria.materia)
        )
        .filter(PlanEstudio.id_plan == id_plan)
        .first()
    )


def actualizar_plan(
    db: Session,
    id_plan: int,
    datos: PlanEstudioUpdate
):
    plan = obtener_plan_por_id(db, id_plan)

    if not plan:
        return None

    for key, value in datos.model_dump(exclude_unset=True).items():
        setattr(plan, key, value)

    db.commit()
    db.refresh(plan)

    return plan


def eliminar_plan(
    db: Session,
    id_plan: int
):
    plan = obtener_plan_por_id(db, id_plan)

    if not plan:
        return None

    db.delete(plan)
    db.commit()

    return plan

def transformar_plan(plan):
    cuatrimestres_dict = {}

    for pm in plan.materias:

        id_cuatri = pm.cuatrimestre.id_cuatrimestre

        if id_cuatri not in cuatrimestres_dict:
            cuatrimestres_dict[id_cuatri] = {
                "id_cuatrimestre": id_cuatri,
                "nombre": pm.cuatrimestre.nombre,
                "materias": []
            }

        cuatrimestres_dict[id_cuatri]["materias"].append({
            "id_plan_materia": pm.id_plan_materia,
            "obligatoria": pm.obligatoria,
            "materia": {
                "id_materia": pm.materia.id_materia,
                "clave": pm.materia.clave,
                "nombre": pm.materia.nombre,
                "creditos": float(pm.materia.creditos)
            }
        })

    return {
        "id_plan": plan.id_plan,
        "nombre_plan": plan.nombre_plan,
        "fecha_inicio": plan.fecha_inicio,
        "fecha_fin": plan.fecha_fin,
        "vigente": plan.vigente,

        "carrera": {
            "id_carrera": plan.carrera.id_carrera,
            "nombre": plan.carrera.nombre
        },

        "cuatrimestres": list(cuatrimestres_dict.values())
    }