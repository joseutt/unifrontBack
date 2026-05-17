from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)
from app.crud.crud_plan_estudio import transformar_plan
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db

from app.schemas.plan_estudio import (
    PlanEstudioCreate,
    PlanEstudioResponse,
    PlanEstudioUpdate
)

from app.crud.crud_plan_estudio import (
    crear_plan_estudio,
    obtener_planes,
    obtener_plan_por_id,
    actualizar_plan,
    eliminar_plan
)

router = APIRouter(
    prefix="/planes-estudio",
    tags=["Planes de Estudio"]
)


@router.post(
    "/",
    response_model=PlanEstudioResponse
)
def crear(
    plan: PlanEstudioCreate,
    db: Session = Depends(get_db)
):
    return crear_plan_estudio(db, plan)


@router.get("/")
def listar(
    db: Session = Depends(get_db)
):
    planes = obtener_planes(db)

    return [
        transformar_plan(plan)
        for plan in planes
    ]


@router.get("/{id_plan}")
def obtener(
    id_plan: int,
    db: Session = Depends(get_db)
):
    plan = obtener_plan_por_id(db, id_plan)

    if not plan:
        raise HTTPException(
            status_code=404,
            detail="Plan no encontrado"
        )

    return transformar_plan(plan)


@router.put(
    "/{id_plan}",
    response_model=PlanEstudioResponse
)
def actualizar(
    id_plan: int,
    datos: PlanEstudioUpdate,
    db: Session = Depends(get_db)
):
    plan = actualizar_plan(
        db,
        id_plan,
        datos
    )

    if not plan:
        raise HTTPException(
            status_code=404,
            detail="Plan de estudio no encontrado"
        )

    return plan


@router.delete(
    "/{id_plan}"
)
def eliminar(
    id_plan: int,
    db: Session = Depends(get_db)
):
    plan = eliminar_plan(db, id_plan)

    if not plan:
        raise HTTPException(
            status_code=404,
            detail="Plan de estudio no encontrado"
        )

    return {
        "message": "Plan eliminado correctamente"
    }