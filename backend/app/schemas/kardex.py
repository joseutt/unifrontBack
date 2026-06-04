from pydantic import BaseModel, Field
from typing import List


class KardexMateria(BaseModel):
    clave: str = ""
    asignatura: str = ""
    creditos: float = 0
    calificacion_final: float = 0


class KardexCuatrimestre(BaseModel):
    cuatrimestre: int = 0
    periodo_escolar: str = ""
    grupo: str = ""
    materias: List[KardexMateria] = Field(default_factory=list)

class KardexResponse(BaseModel):
    matricula: str = ""
    primer_apellido: str = ""
    segundo_apellido: str = ""
    nombre: str = ""
    carrera: str = ""
    plan_estudios: str = ""
    historial: List[KardexCuatrimestre] = Field(default_factory=list)