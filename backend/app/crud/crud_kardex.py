from __future__ import annotations

from collections import defaultdict

from sqlalchemy.orm import Session, joinedload

from app.models.alumno import Alumno
from app.models.carga_academica import CargaAcademica
from app.models.grupo import Grupo
from app.models.grupo_materia import GrupoMateria
from app.models.historial_academico import HistorialAcademico


def _split_nombre(apellido_paterno: str | None, apellido_materno: str | None):
    return apellido_paterno or "", apellido_materno or ""


def get_kardex_by_matricula(db: Session, matricula: str):
    alumno = (
        db.query(Alumno)
        .options(
            joinedload(Alumno.usuario),
            joinedload(Alumno.carrera),
            joinedload(Alumno.plan),
        )
        .filter(Alumno.matricula == matricula)
        .first()
    )

    if not alumno:
        return None

    usuario = alumno.usuario

    primer_apellido, segundo_apellido = _split_nombre(
        getattr(usuario, "apellido_paterno", None),
        getattr(usuario, "apellido_materno", None),
    )

    cargas = (
        db.query(CargaAcademica)
        .options(
            joinedload(CargaAcademica.grupo_materia)
            .joinedload(GrupoMateria.grupo)
            .joinedload(Grupo.cuatrimestre),

            joinedload(CargaAcademica.grupo_materia)
            .joinedload(GrupoMateria.materia),

            joinedload(CargaAcademica.grupo_materia)
            .joinedload(GrupoMateria.periodo),
        )
        .filter(CargaAcademica.id_alumno == alumno.id_alumno)
        .all()
    )

    historial_map = defaultdict(list)

    ids_materias = [
        c.grupo_materia.id_materia
        for c in cargas
        if c.grupo_materia and c.grupo_materia.materia
    ]

    ids_periodos = [
        c.grupo_materia.id_periodo
        for c in cargas
        if c.grupo_materia and c.grupo_materia.periodo
    ]

    historial_rows = (
        db.query(HistorialAcademico)
        .filter(
            HistorialAcademico.id_alumno == alumno.id_alumno,
            HistorialAcademico.id_materia.in_(ids_materias) if ids_materias else False,
            HistorialAcademico.id_periodo.in_(ids_periodos) if ids_periodos else False,
        )
        .all()
    )

    historial_lookup = {}

    for h in historial_rows:
        if h.calificacion_final is None:
            continue

        historial_lookup[
            (h.id_materia, h.id_periodo)
        ] = float(h.calificacion_final)

    for carga in cargas:
        gm = carga.grupo_materia

        if not gm:
            continue

        if not gm.grupo:
            continue

        if not gm.materia:
            continue

        if not gm.periodo:
            continue

        cuatrimestre_num = 0

        if gm.grupo.cuatrimestre:
            cuatrimestre_num = gm.grupo.cuatrimestre.numero

        periodo_escolar = gm.periodo.nombre or ""
        grupo_nombre = gm.grupo.nombre or ""

        calificacion_final = historial_lookup.get(
            (gm.id_materia, gm.id_periodo),
            0.0
        )

        historial_map[
            (
                cuatrimestre_num,
                periodo_escolar,
                grupo_nombre
            )
        ].append(
            {
                "clave": gm.materia.clave or "",
                "asignatura": gm.materia.nombre or "",
                "creditos": float(gm.materia.creditos or 0),
                "calificacion_final": float(calificacion_final),
            }
        )

    historial = []

    for (
        cuatrimestre_num,
        periodo_escolar,
        grupo_nombre,
    ) in sorted(
        historial_map.keys(),
        key=lambda x: (x[0], x[1], x[2]),
    ):
        historial.append(
            {
                "cuatrimestre": cuatrimestre_num,
                "periodo_escolar": periodo_escolar,
                "grupo": grupo_nombre,
                "materias": historial_map[
                    (
                        cuatrimestre_num,
                        periodo_escolar,
                        grupo_nombre,
                    )
                ],
            }
        )

    return {
        "matricula": alumno.matricula or "",
        "primer_apellido": primer_apellido,
        "segundo_apellido": segundo_apellido,
        "nombre": getattr(usuario, "nombre", "") if usuario else "",
        "carrera": alumno.carrera.nombre if alumno.carrera else "",
        "plan_estudios": (
            alumno.plan.nombre_plan
            if alumno.plan
            else ""
        ),
        "historial": historial,
    }